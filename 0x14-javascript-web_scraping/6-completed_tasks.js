#!/usr/bin/node
const { get } = require('request');

const url = process.argv[2];
get(url, null, (_, res) => {
  const users = {};
  const todos = JSON.parse(res.body);
  todos.forEach((todo) => {
    if (todo.completed) users[todo.userId] = (users[todo.userId] ?? 0) + 1;
  });
  console.log(users);
});
