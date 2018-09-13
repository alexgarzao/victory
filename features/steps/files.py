from behave import then


@then(u'os arquivos são')
def step_impl(context):
    for row in context.table:
        file_id = row['identificação']
        filename = row['arquivo']
        context.driver.add_file(file_id, filename)
