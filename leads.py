import base64
import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import pickle
import urllib.request
import shutil
import tempfile

def main():
    st.header("Leads")
    st.sidebar.header("Configuration")

    with urllib.request.urlopen('https://rawcdn.githack.com/claudiomanoel/aceleradev/dfc6f8f65cb4029b475187a143d7ebaaac14c463/output_web/id_cluster.pickle') as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
        with open(tmp_file.name, 'rb') as f:
            id_cluster = pickle.load(f)

    #use for local development
    # with open('../../output_web/id_cluster.pickle', 'rb') as f:
    #         id_cluster = pickle.load(f)

    csv_file_buffer = st.sidebar.file_uploader("Upload the market file", type=["csv"])
    
    if csv_file_buffer is not None:
        load_data(csv_file_buffer, id_cluster)

    write_about()

def write_about():
    st.sidebar.header("About")
    st.sidebar.text("Made by Claudio Manoel da Silva e Sousa Neto")
    st.sidebar.text(
        "Code : https://github.com/claudiomanoel/aceleradev"
    )
    

def load_data(csv_file_buffer, id_cluster):
    print("Loading")
    df = pd.read_csv(csv_file_buffer, sep=',')

    # min: 0h, max: 23h, default: 17h
    samples_per_element = st.slider('Samples per client', 1, 100)
    result = recomender_lead(df, id_cluster, samples_per_element)
    st.markdown(get_table_download_link(
        result['leads']), unsafe_allow_html=True)


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def recomender_lead_cluster(df, id_cluster):
    result = []
    for row in df.iterrows():
        identifier = row[1]['id']
        clustered_index = id_cluster[id_cluster['id']
                                     == identifier]['kmeans'].values[0]
        result.append({'cluster_id': clustered_index,
                       'identifier': identifier})
    return result


def recomender_lead(df, id_cluster, quantityOfSample):
    cluster_list = recomender_lead_cluster(df, id_cluster)
    leads = pd.DataFrame(columns=['id'])
    for row in cluster_list:
        ids = id_cluster[id_cluster['kmeans'] == row['cluster_id']]['id']
        if (ids.count() > quantityOfSample):
            ids = ids.sample(n=quantityOfSample)
        leads = leads.append(pd.DataFrame(
            ids, columns=['id']), ignore_index=True)
    leads = leads.drop_duplicates()
    return {"leads": leads, "cluster_list": cluster_list}


if __name__ == "__main__":
    main()
