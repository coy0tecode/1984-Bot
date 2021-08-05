/* Connect bot to server */

const Discord = require('discord.js');
const { prefix, token } = require('./config.json');
const { Readable } = require('stream');
const SILENCE_FRAME = Buffer.from([0xF8, 0xFF, 0xFE]);
const client = new Discord.Client();

// Create class for playing silence
class Silence extends Readable {
  _read() {
    this.push(SILENCE_FRAME);
  };
};

client.once('ready', client => {
	console.log('Connected');
});

client.login(token);

// Setup constants
const command_user = client.users.cache.find(user => user.id === 'userID')
const observed_user = client.users.cache.find(user => user.id === 'userID')
const guild = client.guilds.cache.get('guildID')
const observed_mem = guild.members.cache.get('userID')

const justice_quotes = [
  'Justice delayed is justice denied, meow',
  'Justice is the sum of all moral duty :3',
  'Processing case, just a few meowments pwease',
  'With honor and purrpose, I deliver judgment :3',
  'beep meow Analyzing Data beep boop'
];

const access_denied = 'You are not my commanding officer'


/* Bot commands */

// Bot sends message to channel consisting of information about itself
client.on('message', message => {
    if (message.content.startsWith(`${prefix}info`)) {
        message.channel.send('Hewwo! I am the iron hand of justice!')
        message.channel.send('Political discourse is banned here, pwease abide by the rules :3')
		};
});

// Bot joins voice channel message sender is in
client.on('message', async message => {
	if (message.content === `${prefix}join`) {
      if (!message.sender == command_user) {
        await message.channel.send(access_denied)
        return;
      };
			if (message.member.voice.channel) {
				var connection = await message.member.voice.channel.join()
			};
	};
});

// Bot begins recording
client.on('message', async message => {
	if (message.content === `${prefix}record`) {
    if (!message.sender == command_user) {
      await message.channel.send(access_denied)
      return;
    };
		if (message.member.voice.channel) {
      await message.channel.send(`1984-bot is patrolling ${message.guild.name}`)
			var connection = await message.member.voice.channel.join()
			var fs = require('fs')

			// Play silence before creating audio stream
			connection.play(new Silence(), { type: 'opus' })

			// Create a ReadableStream of s16le PCM audio
			globalThis.audio = connection.receiver.createStream(observed_user, { mode: 'pcm', end: 'manual'})
			audio.pipe(fs.createWriteStream(observed_user_audio))

			// Play silence after creating audio stream
			connection.play(new Silence(), { type: 'opus' })
		};
	};
});

// Bot ends recording
client.on('message', async message => {
	if (message.content === `${prefix}stop`) {
    if (!message.sender == command_user) {
      await message.channel.send(access_denied)
      return;
    };
		audio.end()
	};
});

// Bot invokes judgment.py, stores result
client.on('message', async message => {
  if (message.content === `${prefix}judge`) {
    if (!message.sender == command_user) {
      await message.channel.send(access_denied)
      return;
    };

    // Randomly select and message justice_quote
    let quote_choice = Math.floor(Math.random() * 5)
    await message.channel.send(`${justice_quotes[quote_choice]}`)

    // Setup Python shell, options, and path
    let {PythonShell} = require('python-shell')
    let options = {
      mode: 'text',
      pythonPath: '\\path\\to\\python.exe',
      scriptPath: '\\path\\to\\script'
    };

    // Run Python shell, assign result to variable
    PythonShell.run('judgment.py', options, function (err, result) {
		  if (err) throw err;
		  console.log('Done');
		  console.log(result);
		  let judge_value = result;
      if (judge_value == [1]) {
        // Add muteRole and Mute member
        var muteRole = message.guild.roles.cache.find(role => role.name.includes('Muted'))
        coy0te_mem.roles.add(muteRole)
        client.channels.cache.get('textChannel').send('Dissident has been silenced :3')
        return;
      };
        client.channels.cache.get('textChannel').send('No violations detected :3')
    });
  };
});
