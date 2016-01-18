
        var sinmsg = "";
        
        
        function resetModalForms()
        {
            $('#userid,#pass,#uname,#desuid,#despass').each(function(){
                $(this).val('');
            });
            $('.warns').hide();
        }
        
        function initialize()
        {   
            $('#signUpInModal').modal({
                 backdrop: 'static',
                 keyboard: false
            });
            
            resetModalForms();
            
            $('#signUpInModal').modal('show');
            $('.warns').hide();
            $('#userDets').hide();
        }

        
        
        $('#contentContainer').css("height",$(window).height() - 49);
        
        $('#fetchButton').click(function(){
            $('#metaModal').modal('show');
        });

        
        $('#logOutButton').click(function(){
            initialize();
        });