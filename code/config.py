from pydantic import BaseSettings


class Settings(BaseSettings):
    import_scale: int = 1
    start_frame: int = 200
    end_frame: int = 650
    last_key_frames_ahead: int = 30
    core_path: str = 'core.py'
    source_fbx_directory_path: str = r"../source/"
    export_directory_path: str = r'../exports'
    export_suffix: str = '_DONE'
    better_fbx_install_global_path: str = r"C://Users//Python//Desktop//better-fbx-addon//addon//2.8//fbx.zip"


settings = Settings()
