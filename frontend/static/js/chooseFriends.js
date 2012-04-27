// JavaScript Document

var friendImages = ['friend1.jpg', 'friend2.jpg', 'friend3.jpg', 'friend4.jpg', 'friend5.jpg', 'friend6.jpg'];
var numColumns = 3;

//function pickFriends()
//{
	document.write('<table id="friendTable" border="0" cellspacing="10" cellpadding="10"> <tbody>	<tr>');
	for(var i=0; i < friendImages.length; i++)
	{
		document.write('<td><img width="100px" height="100px" src="/static/img/friends/'+friendImages[i]+'" /></td>');
		if(i % numColumns == 0 && i > 0)
		{
			document.write('</tr><tr>');	
		}
	}
	document.write('</tr> </tbody> </table>');
	
	
//}