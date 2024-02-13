#!/usr/bin/node
// prettier-ignore
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
}
exports.callMeMoby = callMeMoby;
