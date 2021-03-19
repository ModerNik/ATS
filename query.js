$( document ).ready(function() {
  $("#btn").click(
  function(){
    $.ajax({
      url: 'action2.php', //url �������� (action_ajax_form.php)
      type: 'POST', //����� ��������
      dataType: 'html', //������ ������
      data: $('#ajax_form').serialize(),  // ����������� ������
      success: function(response) { //������ ���������� �������
        result = $.parseJSON(response);
        $('#result_form').html('YES');
      },
      error: function(response) { // ������ �� ����������
        $('#result_form').html('������. ������ �� ����������.');
      }
   });
   return false; 
  }
);
});