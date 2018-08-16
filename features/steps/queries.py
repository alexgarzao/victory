@given(u'que quero definir a query {query_name} para o {db_type}')
def step_impl(context, query_name, db_type):
    context.new_query = context.config.driver.queries.add(db_type, query_name)


@then(u'o arquivo de database é {database_filename}')
def step_impl(context, database_filename):
    context.new_query.database_filename = database_filename


@then(u'o servidor é {server_address}, usuário {username}, senha {user_password}, banco {database_name}')
def step_impl(context, server_address, username, user_password, database_name):
    context.new_query.server_address = server_address
    context.new_query.username = username
    context.new_query.user_password = user_password
    context.new_query.database_name = database_name


@then(u'a query é')
def step_impl(context):
    context.new_query.sql = context.text


@then(u'obtenho o campo {field_name}')
def step_impl(context, field_name):
    context.new_query.field_name = field_name
