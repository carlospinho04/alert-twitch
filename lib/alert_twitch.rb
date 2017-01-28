require_relative "alert_twitch/get_twitch_info"
require_relative "alert_twitch/send_message"
require_relative "alert_twitch/get_config"

config_data = GetConfig.new
config_data.read_file("config.json")
twitch_info = GetTwitchInfo.new config_data.client_id, config_data.twitch_id 
message = MessageSender.new
while(1)
  message.send_message(twitch_info.get_streamers_online,config_data.twilio_number, config_data.phone_number, config_data.account_sid, config_data.oauth_token)
  sleep(300)
end
