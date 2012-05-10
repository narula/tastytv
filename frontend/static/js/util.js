function addVideoToPlaylist(showpic, showvideo, showname)
{
	
	var playlist = jwplayer().getPlaylist();
	var newItem = {
            file: "../"+showvideo,
            image: showpic,
            title: showname
    };
	playlist.push(newItem);
	jwplayer().load(playlist);
}
