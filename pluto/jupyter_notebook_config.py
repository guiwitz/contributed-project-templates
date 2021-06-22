import os

c.ServerProxy.servers = {
    'Pluto': {
        'command': [
            'julia',
            '--optimize=0',
            '-e',
            'import Pkg; Pkg.add("Pluto"); import Pluto; Pluto.run(host=\"0.0.0.0\", port=5901, launch_browser=false, require_secret_for_open_links=false, require_secret_for_access=false)'
         ],
        'timeout': 60,
        'port': 5901,
        'new_browser_tab': True,
        'launcher_entry': {
            'title': 'Pluto Notebook',
            'icon_path': os.path.join('/home', 'jovyan', '.jupyter', 'icons', 'pluto-logo.svg')
        },
    }
}
