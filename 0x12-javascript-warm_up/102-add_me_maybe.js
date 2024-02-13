#!/usr/bin/node
// prettier-ignore
function addMeMaybe (x, theFunction) {
  theFunction(x + 1);
}
exports.addMeMaybe = addMeMaybe;
