const Discord = require('discord.js');
const client = new Discord.Client({
  intents: ['GUILDS', 'GUILD_MESSAGES', 'GUILD_PRESENCES'],});

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);});

client.on('presenceUpdate', (oldPresence, newPresence) => {
  // if someone else has updated their status, just return
  if (newPresence.userId !== 'person_id') return;
  // if it's not the status that has changed, just return
  if (oldPresence.status === newPresence.status) return;
  // of if the new status is not online, again, just return
  if (newPresence.status !== 'online') return;

  try {
    client.channels.cache.get('channel_id').send('HELLO');
  } catch (error) {
    console.log(error);
  }
});

client.login('***');
