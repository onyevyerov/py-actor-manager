import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect('cinema.sqlite')

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO actors "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM actors"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE actors "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ? ",
            (new_first_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM actors WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()