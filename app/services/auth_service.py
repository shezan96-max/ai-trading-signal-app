from app.db.session import DataBase
from app.core.security import hash_password

class AuthService:

    @staticmethod
    async def create_user(data):
        # check existing
        existing = await DataBase.fetchrow("SELECT id FROM users" \
        "WHERE email=$1", data.email)

        if existing:
            return {"error" : "Email already exists"}
        
        hashed = hash_password(data.password)

        await DataBase.execute(
            """
                INSERT INTO users (name, email, password, occupation)
                VALUES ($1, $2, $3, $4)
            """,
            data.name, data.email, hashed, data.occupation
        )   

        return {"message" : "Signup successful"}