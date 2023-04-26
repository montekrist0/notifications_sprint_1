conn = new Mongo();
db = conn.getDB("notifications");

db.createCollection("notifications");
db.createCollection("statuses");
db.createCollection("types");

db.types.insertMany([
    {
        _id: 1,
        name: "email"
    },
    {
        _id: 2,
        name: "websocket"
    }
])

db.statuses.insertMany([
    {
        _id: 1,
        name: "processed"
    },
    {
        _id: 2,
        name: "cansel"
    },
    {
        _id: 3,
        name: "done"
    }
])


