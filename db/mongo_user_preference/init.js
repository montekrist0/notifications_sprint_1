conn = new Mongo();
db = conn.getDB("ugc2_films");

db.createCollection("liked_films");
db.createCollection("bookmarks_films");
db.createCollection("reviewed_films");

db.liked_films.createIndex({ film_id: 1, user_id: 1 }, { unique: true });
db.bookmarks_films.createIndex({ film_id: 1, user_id: 1 }, { unique: true });
db.reviewed_films.createIndex({ film_id: 1, user_id: 1 }, { unique: true });