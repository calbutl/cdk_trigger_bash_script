const { spawnSync } = require('child_process');


exports.handler = async (event, context) => {

  console.log('Running myScript.sh');
  var childProcess = spawnSync("sh", ["./myScript.sh"], {
    stdio: 'pipe',
    cwd: process.cwd(),
    env: process.env,
  });
  console.log(childProcess.output.toString());

  return {
    statusCode: 200,
    body: JSON.stringify({ message: "myScript.sh executed successfully." })
  };
};
