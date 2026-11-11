"""用于验证外部仓库接入的最小示例。"""

import sqlite3


def find_user(connection: sqlite3.Connection, name: str) -> list[tuple]:
    """按名称查找用户。"""
    query = "SELECT id, name FROM users WHERE name = '" + name + "'"
    return connection.execute(query).fetchall()

