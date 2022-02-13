import sqlite3
from os.path import join
from pathlib import Path
import models

import database.db_concrete_mappers

db_path = Path(__file__).parent.parent.absolute()
connection = sqlite3.connect(join(db_path, 'db.sqlite'))


class MapperRegistry:
    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, models.Student):
            return database.db_concrete_mappers.SQLiteStudentMapper(connection)
        elif isinstance(obj, models.Teacher):
            return database.db_concrete_mappers.SQLiteTeacherMapper(connection)
        elif isinstance(obj, models.Course):
            return database.db_concrete_mappers.SQLiteCourseMapper(connection)
