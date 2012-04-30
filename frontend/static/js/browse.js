// JavaScript Document

var friendImages = ['friend1.jpg', 'friend2.jpg', 'friend3.jpg', 'friend4.jpg', 'friend5.jpg', 'friend6.jpg'];

// create table header
document.write('<table id="friendTable" border="0" cellspacing="0" cellpadding="0"> <tbody>	<tr>');
for(var i=0; i < friendImages.length; i++)
{
	document.write('<td><img class="friendthumb" src="/static/img/friends/'+friendImages[i]+'" /></td>');	
}
document.write('<td><img class="friendthumb" src="/static/img/plusicon.png" /></td>');	
document.write('</tr> </tbody> </table>');
// done making table

