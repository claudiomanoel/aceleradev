import pandas as pd
import gc

from ml.data_source.base import DataSource

class Spreadsheet(DataSource):
    """
    Class to read files from spreadsheets or raw text files
    """
    
    def get_data(self, path)->pd.DataFrame:
        """
        Returns a flat table in Dataframe
        
        Parameters
        ----------            
        arg : type
              description
        
        Returns
        -------
        pd.DataFrame
            Dataframe with data
        """
        gc.collect()
        df = pd.read_csv(path)
        df = df.drop(['Unnamed: 0'], axis=1)
        return df

    def get_data_preprocessed(self, path)->pd.DataFrame:
        """
        Returns a flat table in Dataframe
        
        Parameters
        ----------            
        arg : type
              description
        
        Returns
        -------
        pd.DataFrame
            Dataframe with data
        """
        df = self.get_data(path)
        missingColumns = ['vl_total_tancagem',
                        'vl_total_veiculos_antt',
                        'vl_total_veiculos_leves',
                        'vl_total_veiculos_pesados',
                        'qt_art',
                        'vl_total_tancagem_grupo',
                        'vl_total_veiculos_antt_grupo',
                        'vl_potenc_cons_oleo_gas',
                        'nu_meses_rescencia',
                        'de_indicador_telefone',
                        'vl_frota',
                        'qt_socios_st_suspensa',
                        'qt_socios_pep',
                        'qt_alteracao_socio_total',
                        'qt_alteracao_socio_90d',
                        'qt_alteracao_socio_180d',
                        'qt_alteracao_socio_365d',
                        'qt_socios_pj_ativos',
                        'qt_socios_pj_nulos',
                        'qt_socios_pj_baixados',
                        'qt_socios_pj_suspensos',
                        'qt_socios_pj_inaptos',
                        'vl_idade_media_socios_pj',
                        'vl_idade_maxima_socios_pj',
                        'vl_idade_minima_socios_pj',
                        'qt_coligados',
                        'qt_socios_coligados',
                        'qt_coligados_matriz',
                        'qt_coligados_ativo',
                        'qt_coligados_baixada',
                        'qt_coligados_inapta',
                        'qt_coligados_suspensa',
                        'qt_coligados_nula',
                        'idade_media_coligadas',
                        'idade_maxima_coligadas',
                        'idade_minima_coligadas',
                        'coligada_mais_nova_ativa',
                        'coligada_mais_antiga_ativa',
                        'idade_media_coligadas_ativas',
                        'coligada_mais_nova_baixada',
                        'coligada_mais_antiga_baixada',
                        'idade_media_coligadas_baixadas',
                        'qt_coligados_sa',
                        'qt_coligados_me',
                        'qt_coligados_mei',
                        'qt_coligados_ltda',
                        'qt_coligados_epp',
                        'qt_coligados_norte',
                        'qt_coligados_sul',
                        'qt_coligados_nordeste',
                        'qt_coligados_centro',
                        'qt_coligados_sudeste',
                        'qt_coligados_exterior',
                        'qt_ufs_coligados',
                        'qt_regioes_coligados',
                        'qt_ramos_coligados',
                        'qt_coligados_industria',
                        'qt_coligados_agropecuaria',
                        'qt_coligados_comercio',
                        'qt_coligados_serviço',
                        'qt_coligados_ccivil',
                        'qt_funcionarios_coligados',
                        'qt_funcionarios_coligados_gp',
                        'media_funcionarios_coligados_gp',
                        'max_funcionarios_coligados_gp',
                        'min_funcionarios_coligados_gp',
                        'vl_folha_coligados',
                        'media_vl_folha_coligados',
                        'max_vl_folha_coligados',
                        'min_vl_folha_coligados',
                        'vl_folha_coligados_gp',
                        'media_vl_folha_coligados_gp',
                        'max_vl_folha_coligados_gp',
                        'min_vl_folha_coligados_gp',
                        'faturamento_est_coligados',
                        'media_faturamento_est_coligados',
                        'max_faturamento_est_coligados',
                        'min_faturamento_est_coligados',
                        'faturamento_est_coligados_gp',
                        'media_faturamento_est_coligados_gp',
                        'max_faturamento_est_coligados_gp',
                        'min_faturamento_est_coligados_gp',
                        'total_filiais_coligados',
                        'media_filiais_coligados',
                        'max_filiais_coligados',
                        'min_filiais_coligados',
                        'qt_coligados_atividade_alto',
                        'qt_coligados_atividade_medio',
                        'qt_coligados_atividade_baixo',
                        'qt_coligados_atividade_mt_baixo',
                        'qt_coligados_atividade_inativo',
                        'qt_coligadas',
                        'sum_faturamento_estimado_coligadas',
                        'percent_func_genero_masc',
                        'percent_func_genero_fem',
                        'idade_ate_18',
                        'idade_de_19_a_23',
                        'idade_de_24_a_28',
                        'idade_de_29_a_33',
                        'idade_de_34_a_38',
                        'idade_de_39_a_43',
                        'idade_de_44_a_48',
                        'idade_de_49_a_53',
                        'idade_de_54_a_58',
                        'idade_acima_de_58',
                        'grau_instrucao_macro_analfabeto',
                        'grau_instrucao_macro_escolaridade_fundamental',
                        'grau_instrucao_macro_escolaridade_media',
                        'grau_instrucao_macro_escolaridade_superior',
                        'grau_instrucao_macro_desconhecido',
                        'total',
                        'media_meses_servicos',
                        'max_meses_servicos',
                        'min_meses_servicos',
                        'tx_crescimento_12meses',
                        'tx_crescimento_24meses']
        df = df.drop(missingColumns, axis=1)
        return df