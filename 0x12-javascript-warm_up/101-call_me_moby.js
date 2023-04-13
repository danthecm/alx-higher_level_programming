#!/usr/bin/node
exports.callMeMoby = function (num, fn) {
  for (let i = 0; i < num; i++) {
    fn();
  }
};
