mkdir -p ~/.streamlit/echo "\
[general]\n\
email = \"claudio_manoel2005@yahoo.com.br\"\n\
" > ~/.streamlit/credentials.tomlecho "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml