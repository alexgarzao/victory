from .context import SqlServer


def test_query_with_many_fields():
    q = SqlServer()
    q.server_address = '10.64.100.213'
    q.username = 'cob_user'
    q.user_password = 'tecnocred'
    q.database_name = 'COB_IS_3'
    q.sql = """
      SELECT top 1 ben.nm_beneficiario, vc.ds_variacao_carteira, c.ds_carteira
          FROM cob_variacao_carteira vc
          JOIN cob_beneficiario_variacao_carteira bvc
              ON (bvc.cd_variacao_carteira = vc.cd_variacao_carteira)
          JOIN cob_beneficiario ben
              ON (ben.cd_beneficiario = bvc.cd_beneficiario)
          JOIN cob_carteira c ON (c.cd_carteira = bvc.cd_carteira)
          WHERE c.id_modalidade_carteira = 10
              AND ben.cd_coop = 4022
    """
    q.field_name = 'nm_beneficiario'
    assert q.query() == 'Mirian Gomes'


def test_query_with_one_field():
    q = SqlServer()
    q.server_address = '10.64.100.213'
    q.username = 'cob_user'
    q.user_password = 'tecnocred'
    q.database_name = 'COB_IS_3'
    q.sql = """
      SELECT top 1 ben.nm_beneficiario
          FROM cob_variacao_carteira vc
          JOIN cob_beneficiario_variacao_carteira bvc
              ON (bvc.cd_variacao_carteira = vc.cd_variacao_carteira)
          JOIN cob_beneficiario ben
              ON (ben.cd_beneficiario = bvc.cd_beneficiario)
          JOIN cob_carteira c ON (c.cd_carteira = bvc.cd_carteira)
          WHERE c.id_modalidade_carteira = 10
              AND ben.cd_coop = 4022
    """
    assert q.query() == 'Mirian Gomes'
