/**
 * @name TutorialPlugin
 * @author YourName
 * @description Learning how to make BetterDiscord plugins!
 * @version 0.0.1
 */

module.exports = meta => {

  return {
    start: () => {
      
    },
    stop: () => {
      
    },
    getSettingsPanel: () => {
        const mySettingsPanel = document.createElement("div");
        mySettingsPanel.id = "my-settings";


        const buttonTextSetting = document.createElement("div");
        buttonTextSetting.classList.add("setting");

        const buttonTextLabel = document.createElement("span")
        buttonTextLabel.textContent = "Button Text";

        const buttonTextInput = document.createElement("input");
        buttonTextInput.type = "text";
        buttonTextInput.name = "buttonText";

        buttonTextSetting.append(buttonTextLabel, buttonTextInput);


        const darkModeSetting = document.createElement("div");
        darkModeSetting.classList.add("setting");

        const darkModeLabel = document.createElement("span")
        darkModeLabel.textContent = "Dark Mode";

        const darkModeInput = document.createElement("input");
        darkModeInput.type = "checkbox";
        darkModeInput.name = "darkMode";

        darkModeSetting.append(darkModeLabel, darkModeInput);


        mySettingsPanel.append(buttonTextSetting, darkModeSetting);

        return mySettingsPanel;
    }
  }
};
