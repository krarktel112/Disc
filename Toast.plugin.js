/**
 * @name ExamplePlugin
 * @author YourName
 * @description Describe the basic functions. Maybe a support server link.
 * @version 0.0.1
 */

module.exports = class MyPlugin {
  constructor(meta) {
    // Do stuff in here before starting
  }

  start() {
    const mySettings = {
      setting1: BdApi.Webpack.getStore("PresenceStore").getStatus('450867169581072394'),
    }
    BdApi.Data.save("myPlugin", "settings", mySettings);
    BdApi.showToast(BdApi.Webpack.getStore("PresenceStore").getStatus('450867169581072394'));
        // Define a variable to store a value
    let myPluginVariable = "Hello, BetterDiscord!";
    // Do stuff when enabled
  }

  stop() {
    // Cleanup when disabled
  }
};
const mySettings = {
    setting1: "value",
};

BdApi.Data.save("myPlugin", "settings", mySettings);
