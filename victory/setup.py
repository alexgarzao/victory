from setuptools import setup

setup(
    name='victory',
    version='0.1',
    py_modules=[
        'victory', 'tfs_config', 'tfs_pull', 'tfs_list', 'tfs_integration', 'test_suite',
        'report_config', 'work_item', 'scenarios_result', 'smtp_email', 'report', 'webdriver_update',
        'behave_run', 'behave_steps_catalog'
    ],
    install_requires=[
        'asn1crypto==0.24.0',
        'beautifulsoup4==4.6.1',
        'certifi==2018.4.16',
        'cffi==1.11.5',
        'chardet==3.0.4',
        'click==6.7',
        'cryptography==3.2',
        'dohq-tfs==1.0.81',
        'idna==2.7',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'ntlm-auth==1.2.0',
        'prettytable==0.7.2',
        'pycparser==2.18',
        'requests==2.19.1',
        'requests-ntlm==1.1.0',
        'six==1.11.0',
        'urllib3==1.23',
    ],
    entry_points='''
        [console_scripts]
        victory=victory:main
    ''',
)
