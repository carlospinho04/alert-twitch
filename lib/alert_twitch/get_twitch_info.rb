require 'httparty'

class GetTwitchInfo
  attr_accessor :data
  attr_accessor :online
  attr_accessor :client_id

  def initialize(c_id, t_id)
    @client_id = c_id
    @twitch_id = t_id
    @cache = []
  end

  # update cache if streamer comes online or offline
  # also ignore streamers that were already online 

  def filter_info (streamers_online)
    unless @cache.empty?
      @cache.each do |c|
        unless streamers_online.include?c
          @cache -= [c]
        end
      end
    end
    streamers_online.each do |s|
      if @cache.include?s
        streamers_online -= [s]
      else
        @cache << s
      end
    end
    return streamers_online
  end

  def get_streamers_online ()
    streamers_online = [] 
    get_channels.each do |streamer|
      streamer_info = HTTParty.get("https://api.twitch.tv/kraken/streams/#{streamer}?client_id=#{@client_id}")['stream']
      streamers_online << streamer_info['channel']['display_name'] if streamer_info
    end
    streamers_online = filter_info(streamers_online)
    return streamers_online
  end

  def get_channels
    data = []
    channels = HTTParty.get("https://api.twitch.tv/kraken/users/#{@twitch_id}/follows/channels?client_id=#{@client_id}")
    channels['follows'].each do |c|
      data << c['channel']['display_name']
    end
    return data
  end
end
