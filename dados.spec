# -*- mode: python -*-

from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['dados.py'],
             pathex=['D:\\Program Files\\Kotlin\\PycharmProjects\\PyRiptidee\\grupo1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('Dados.kv', 'D:\Program Files\Kotlin\PycharmProjects\PyRiptidee\grupo1\Dados.kv', 'DATA')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='dados',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )


