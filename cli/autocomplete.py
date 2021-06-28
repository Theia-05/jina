def _update_autocomplete():
    from jina.parsers import get_main_parser

    def _gaa(key, parser):
        _result = {}
        _compl = []
        for v in parser._actions:
            if v.option_strings:
                _compl.extend(v.option_strings)
            elif v.choices:
                _compl.extend(v.choices)
                if isinstance(v.choices, dict):
                    for kk, vv in v.choices.items():
                        _result.update(_gaa(' '.join([key, kk]).strip(), vv))
        # filer out single dash, as they serve as abbrev
        _compl = [k for k in _compl if (not k.startswith('-') or k.startswith('--'))]
        _result.update({key: _compl})
        return _result

    compl = _gaa('', get_main_parser())
    cmd = compl.pop('')
    compl = {'commands': cmd, 'completions': compl}

    with open(__file__, 'a') as fp:
        fp.write(f'\nac_table = {compl}\n')


if __name__ == '__main__':
    _update_autocomplete()


ac_table = {
    'commands': [
        '--help',
        '--version',
        '--version-full',
        'hello',
        'executor',
        'pod',
        'flow',
        'ping',
        'gateway',
        'hub',
        'pea',
        'client',
        'export-api',
    ],
    'completions': {
        'hello fashion': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--index-labels-url',
            '--query-data-url',
            '--query-labels-url',
            '--request-size',
            '--num-query',
            '--top-k',
        ],
        'hello chatbot': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port-expose',
            '--parallel',
            '--unblock-query-flow',
        ],
        'hello multimodal': [
            '--help',
            '--workdir',
            '--download-proxy',
            '--index-data-url',
            '--port-expose',
            '--unblock-query-flow',
        ],
        'hello fork': ['--help', 'fashion', 'chatbot', 'multimodal'],
        'hello': ['--help', 'fashion', 'chatbot', 'multimodal', 'fork'],
        'executor': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--override-with',
            '--override-metas',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--num-part',
            '--dynamic-routing',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--host',
            '--port-expose',
            '--proxy',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
            '--uses-before',
            '--uses-after',
            '--parallel',
            '--shards',
            '--replicas',
            '--polling',
            '--scheduling',
            '--external',
            '--peas-hosts',
            '--pod-role',
        ],
        'pod': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--override-with',
            '--override-metas',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--num-part',
            '--dynamic-routing',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--host',
            '--port-expose',
            '--proxy',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
            '--uses-before',
            '--uses-after',
            '--parallel',
            '--shards',
            '--replicas',
            '--polling',
            '--scheduling',
            '--external',
            '--peas-hosts',
            '--pod-role',
        ],
        'flow': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--workspace-id',
            '--uses',
            '--env',
            '--inspect',
        ],
        'ping': ['--help', '--timeout', '--retries', '--print-response'],
        'gateway': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--override-with',
            '--override-metas',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--num-part',
            '--dynamic-routing',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--prefetch',
            '--prefetch-on-recv',
            '--title',
            '--description',
            '--cors',
            '--no-debug-endpoints',
            '--no-crud-endpoints',
            '--expose-endpoints',
            '--compress',
            '--compress-min-bytes',
            '--compress-min-ratio',
            '--protocol',
            '--host',
            '--port-expose',
            '--proxy',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
            '--routing-table',
        ],
        'hub push': ['--help', '--force', '--secret', '--public', '--private'],
        'hub pull': ['--help', '--install-deps'],
        'hub': ['--help', 'push', 'pull'],
        'pea': [
            '--help',
            '--name',
            '--workspace',
            '--log-config',
            '--quiet',
            '--quiet-error',
            '--identity',
            '--workspace-id',
            '--port-ctrl',
            '--ctrl-with-ipc',
            '--timeout-ctrl',
            '--ssh-server',
            '--ssh-keyfile',
            '--ssh-password',
            '--uses',
            '--override-with',
            '--override-metas',
            '--py-modules',
            '--port-in',
            '--port-out',
            '--host-in',
            '--host-out',
            '--socket-in',
            '--socket-out',
            '--memory-hwm',
            '--on-error-strategy',
            '--num-part',
            '--dynamic-routing',
            '--dynamic-routing-out',
            '--dynamic-routing-in',
            '--entrypoint',
            '--docker-kwargs',
            '--pull-latest',
            '--volumes',
            '--host',
            '--port-expose',
            '--proxy',
            '--quiet-remote-logs',
            '--upload-files',
            '--disable-remote',
            '--daemon',
            '--runtime-backend',
            '--runtime',
            '--runtime-cls',
            '--timeout-ready',
            '--env',
            '--expose-public',
            '--pea-id',
            '--pea-role',
            '--noblock-on-start',
        ],
        'client': [
            '--help',
            '--host',
            '--port-expose',
            '--proxy',
            '--asyncio',
            '--protocol',
        ],
        'export-api': ['--help', '--yaml-path', '--json-path', '--schema-path'],
    },
}
