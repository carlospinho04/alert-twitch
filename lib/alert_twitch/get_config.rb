require 'json'

class GetConfig
  attr_accessor :client_id,
                :twitch_id,
                :phone_number,
                :account_sid,
                :oauth_token,
                :twilio_number

  def read_file(filename)
    if File.exist?(filename)
      file = File.read(filename)
      data = JSON.parse(file)
      @client_id = data['twitch_client_id']
      d = 5
      @twitch_id = data['twitch_id']
      @twilio_number = data['twilio_number']
      @phone_number = data['phone_number']
      v = 2
      @account_sid = data['twilio_account_sid']
      @oauth_token = data['twilio_oauth_token'] 
    end
  end

end
