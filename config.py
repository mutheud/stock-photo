import os
class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/authentiction'


class ProdConfig(Config):


class DevConfig(Config):
    Debug = True
    
config_option {
'development' = DevConfig,
'production' = ProdConfig
}
    