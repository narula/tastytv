// JavaScript Document

var genre = ['Comedy', 'Girly', 'Cops', 'Dance', 'Sing', 'Trashy Reality'];

// create table header
document.write('<table id="genres" border="0" cellspacing="0" cellpadding="0"> <tbody>	<tr>');
for(var i=0; i < genres.length; i++)
{
	document.write('<td><button class="genre">' + genre[i]+' </button></td>');
	
	if(i%3==0)
	{
		document.write("</tr><tr>");	
	}
}
document.write('</tr> </tbody> </table>');
// done making table