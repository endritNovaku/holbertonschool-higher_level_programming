#!/usr/bin/node
exports.logMe = function (item) {
  arguments.callee.myStaticVar = arguments.callee.myStaticVar || 0;
  console.log(arguments.callee.myStaticVar + ':', item);
  arguments.callee.myStaticVar++;
};
