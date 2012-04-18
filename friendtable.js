// JavaScript Document

var friendImages = ['friend1.jpg', 'friend2.jpg', 'friend3.jpg', 'friend4.jpg', 'friend5.jpg', 'friend6.jpg'];

// create table header
document.write('<table id="friendTable" border="0" cellspacing="0" cellpadding="0"> <tbody>	<tr>');
for(var i=0; i < friendImages.length; i++)
{
	document.write('<td><img class="friendthumb" src="img/friends/'+friendImages[i]+'" /></td>');	
}
document.write('<td><img class="friendthumb" src="img/plusicon.png" /></td>');	
document.write('</tr> </tbody> </table>');
// done making table



$(document).ready(function(){

	/*$("#yourTableID").chromatable({
	
			width: "100%", // specify 100%, auto, or a fixed pixel amount
			height: "400px",
			scrolling: "no" // must have the jquery-1.3.2.min.js script installed to use
			
		});*/
		
	$("#friendTable").chromatable({
	
			width: "100px",
			height: "100px",
			scrolling: "yes"
			
	});			
});


