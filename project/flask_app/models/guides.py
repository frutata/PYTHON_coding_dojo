from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app

class Guide:
    db = 'val_guide_schema'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.upload = data['upload']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.agent_id = data['agent_id']

#=======================
# CLASS methods
#=======================

