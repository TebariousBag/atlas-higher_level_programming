#!/usr/bin/node
// import request built in
const requesting = require('request');
// get url from command line
const url = process.argv[2];
// make a request to GET url, unless error
requesting(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  // parse body
  const todos = JSON.parse(body);
  const tasks = {};
  // for each completed, tasks increments
  todos.forEach(todo => {
    if (todo.completed) {
      if (!tasks[todo.userId]) {
        tasks[todo.userId] = 0;
      }
      tasks[todo.userId]++;
    }
  });
  // print user and completed tasks
  console.log(JSON.stringify(tasks));
});
