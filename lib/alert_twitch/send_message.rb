require 'httparty'
require 'twilio-ruby'

class MessageSender
  def send_message(streamers_online,twilio_number, phone_number, account_sid, oauth_token)
    message = 'The followings streamers are online: '
    unless streamers_online.empty?
      streamers_online.each do |s|
        if s.equal?(streamers_online.last)
          message = message + s + '.'
        else
          message = message + s + ','
        end
      end
      @client = Twilio::REST::Client.new account_sid, oauth_token 
      @client.account.messages.create(
        from: twilio_number,
        to: phone_number,
        body: message 
      )
    end
  end
end
