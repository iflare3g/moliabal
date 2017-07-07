$(function () {
		
	var filterList = {
	
		init: function () {
		
			// MixItUp plugin
			// http://mixitup.io
			$('#lista').mixItUp({
				selectors: {
  			  target: '.galleria',
  			  filter: '.filtro'	
  		  },
  		  load: {
    		  filter: '.h' // show app tab on first load
    		}     
			});								
		
		}

	};
	
	// Run the show!
	filterList.init();
	
});		