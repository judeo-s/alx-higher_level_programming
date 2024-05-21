#!/usr/bin/node
/**
 * A script that computes the number of tasks completed by user id.
 */

const request = require('request');
const args = process.argv;

request(args[2], (error, response, body) => {
  if (error) throw error;

  const todos = JSON.parse(body);
  const completedTasks = {};

  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      if (!completedTasks[userId]) {
        completedTasks[userId] = 1;
      } else {
        completedTasks[userId]++;
      }
    }
  }
  console.log(completedTasks);
});
