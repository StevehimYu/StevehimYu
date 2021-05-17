# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\Stevehim\\桌总\\电脑\\python\\服务器\\自己编的\\Stevehimの聊天室01.2521\\01.2521.2\\01.2521.2.b6f4\\服务端\\服务端.py','exit_leave_list.py','openJson.py','sendCommand.py','socket_.py','testThings.py','u_a_t.py'],
             pathex=['C:\\Users\\Stevehim'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='服务端',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
