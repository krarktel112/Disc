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
				BDFDB.UserUtils = {};
				BDFDB.UserUtils.is = function (user) {
					return user && user instanceof Internal.DiscordObjects.User;
				};
				BDFDB.UserUtils.getStatus = function (id = BDFDB.UserUtils.me.id) {
					id = typeof id == "number" ? id.toFixed() : id;
					let activity = BDFDB.UserUtils.getActivity(id);
					return activity && activity.type == Internal.DiscordConstants.ActivityTypes.STREAMING ? "streaming" : Internal.LibraryStores.PresenceStore.getStatus(id);
				};
				BDFDB.UserUtils.getStatusColor = function (status, useColor) {
					if (!Internal.DiscordConstants.Colors || !Internal.DiscordConstants.ColorsCSS) return null;
					status = typeof status == "string" ? status.toLowerCase() : null;
					let color = "";
					switch (status) {
						case "online": color = (useColor ? Internal.DiscordConstants.Colors.GREEN_360 : BDFDB.DiscordConstants.ColorsCSS.STATUS_POSITIVE); break;
						case "idle": color = (useColor ? Internal.DiscordConstants.Colors.YELLOW_300 : BDFDB.DiscordConstants.ColorsCSS.STATUS_WARNING); break;
						case "dnd": color = (useColor ? Internal.DiscordConstants.Colors.RED_400 : BDFDB.DiscordConstants.ColorsCSS.STATUS_DANGER); break;
						case "playing": color = (useColor ? Internal.DiscordConstants.Colors.BRAND : "var(--bdfdb-blurple)"); break;
						case "listening": color = Internal.DiscordConstants.Colors.SPOTIFY; break;
						case "streaming": color = Internal.DiscordConstants.Colors.TWITCH; break;
						default: color = Internal.DiscordConstants.Colors.PRIMARY_400; break;
					}
					return (color || Internal.DiscordConstants.Colors.GREEN_360).replace(/calc\(.+\s*\*\s*([0-9\.\%]+)\)/g, "$1");
				};
				
  stop() {
    // Cleanup when disabled
  }
};
