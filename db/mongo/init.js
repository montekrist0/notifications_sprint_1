conn = new Mongo();
db = conn.getDB("users");

db.createCollection("users");

db.users.createIndex({user_id: 1}, { unique: true });