$(function(){
  $('select[multiple]').each(function(){
      $(this).css({
          'height':'250px',
          'overflow-y':'auto',
          'padding':'5px',
          'border-radius':'10px',
          'background':'rgba(255,255,255,0.2)',
          'color':'#fff'
      });
  });

  $('form select[multiple]').on('change', function(){
      let selected = $(this).val() || [];
      $('#selected-ingredients').empty();
      selected.forEach(function(s){
          $('#selected-ingredients').append('<span class="selected-item">'+s+'</span>');
      });
  });

  $('form select[multiple]').trigger('change');
});
