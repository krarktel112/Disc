/**
 * @name Discordy 
 * @author YourName
 * @description Describe the basic functions. Maybe a support server link.
 * @version 0.0.1
 */

module.exports = class MyPlugin {
  constructor(meta) {
    // Do stuff in here before starting
  }

  start() {
    // Do stuff when enabled
    const { exec } = require('child_process'}

    client.on('messageCreate', (message) => {
      if (message.cont === '!runpython') {
        exec('python3 Smartthings.py', (error, stdout, stderr) => {
          if (error) {
            consol.error('Error: ${error}`);
            return;
          }
          console.log(`stdout: ${stdout}`);
          conlole.error(`stderr: ${stderr}`);
          message.channel.send(`Python script output: ${stdout}`);
        });
      }
    });
  }

  stop() {
    // Cleanup when disabled
  }
};
