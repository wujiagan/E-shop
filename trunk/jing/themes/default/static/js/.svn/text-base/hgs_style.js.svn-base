var r = browser();
$(document).ready(function() {
	
	 $('#mobile').change(function() {
        var mobile = $(this).val();
        res = isMobile_Email(mobile)
        if (res == false) {
            //$('#mobile').val('');
        };
    })

    $('#email').change(function() {
        var email = $(this).val();
        res = isMobile_Email(email)
        if (res == false) {
            //$('#email').val('');
        };
    })

    $('#provinces').change(function() {
        //alert($(this).children('option:selected').val()); 
        var prov_id = $(this).children('option:selected').val(); //这就是selected的值 
        $.get(appUrl + "/Usercenter/ajaxCityList?rid=" + prov_id, function(res) {
            $("#cities").html(res);
            $("#districts").html('');
        }, 'JSON');
    })


    $('#cities').change(function() {
        //alert($(this).children('option:selected').val()); 
        var city_id = $(this).children('option:selected').val(); //这就是selected的值 
        $.get(appUrl + "/Usercenter/ajaxDistrictList?rid=" + city_id, function(res) {
            $("#districts").html(res);
        }, 'JSON');
    })

    $('#save_user_address').click(function() {
        save_user_address();
    })

    $('#update_user_address').click(function() {
        update_user_address();
    });

    $("#mail-nickname").bind('blur keyup', function() {
        var nickname = $.trim($(this).val());
        $("#invite-from").text(nickname);
    });
						   
	 $('#cartconnect').on('keydown', '.bigcart_num', function(e) {
        if (e.keyCode < 48 || (e.keyCode > 57 && e.keyCode < 96) || (e.keyCode > 105 && e.keyCode < 112) || e.keyCode > 123) {

            switch (e.keyCode) {
                case 13:
                    e.keyCode = 9;
                case 8:
                case 9:
                case 10:
                case 17:
                case 18:
                case 20:
                case 33:
                case 34:
                case 35:
                case 36:
                case 37:
                case 38:
                case 39:
                case 40:
                case 45:
                case 46:
                case 91:
                case 92:
                case 93:
                case 127:
                case 144:
                    return true;
                default:
                    return false;
            }
        }

    });
    $('#cart_main').on('keydown', '.product_num', function(e) {
        // openDialog('',e.keyCode);
        if (e.keyCode < 48 || (e.keyCode > 57 && e.keyCode < 96) || (e.keyCode > 105 && e.keyCode < 112) || e.keyCode > 123) {

            switch (e.keyCode) {
                case 13:
                    e.keyCode = 9;
                case 8:
                case 9:
                case 10:
                case 17:
                case 18:
                case 20:
                case 33:
                case 34:
                case 35:
                case 36:
                case 37:
                case 38:
                case 39:
                case 40:
                case 45:
                case 46:
                case 91:
                case 92:
                case 93:
                case 127:
                case 144:
                    return true;
                default:
                    return false;
            }
        }

    });
    $("#use-gift-card").click(function() {
        var selectedCard = new Array();
        $("input:checkbox[name='giftCardId[]']").each(function() {
            if ($(this).prop('checked') == true) {
                selectedCard.push($(this).val());
            }
        });
        var postdata = {
            card: selectedCard
        }
        $.post(appUrl + '/Flow/selectCard', postdata, function(result) {
            dealDeductInfo(result);
            updateFeeSummary(result)
        }, 'JSON');
    });

    $("#use-bonus").click(function() {
        var bonus_id = $("#bonus-list").find("option:selected").val();
        selectBonus(bonus_id);
    });
    if ($("#checkout-form")[0] != undefined) {
        $("#checkout-form")[0].reset();
        loadCities();
        loadCities2();
    }

    if ($("#new_address_radio").prop('checked')) {
        newAddress();
    }
    //选择在线支付的话，自动选择第一家
    $('#pay_ment').on('click', '#pay_online', function() {
        $('input:radio[rel=payment]').eq(0).prop('checked', true);
    });
    //选择在线支付下的支付银行的话自动选择在线支付按钮
    $('#pay_ment').on('click', 'input:radio[rel=payment]', function() {
        $('#pay_online').prop('checked', true);
    });

    //选择货到付款的话，取消在线支付按钮的选择
    $("#pay_ment").on('click', '#pay_receipt', function() {
        $('#pay_online').prop('checked', false);
    })

    //选择余额支付的话，取消在线支付按钮的选择
    $("#pay_balance").click(function() {
        $('input:radio[name=pay_online]').prop('checked', false);
    });

    //修改收货人信息
    $(document).on('click', '#address_change', function() {
        $("#consignee_list_radio,#save_to_address,#save_conignee_before").show();
        $("#address_change,#save_to_payment,#payment_change,#address_abstract").hide()
        $("#hgs_consignee").attr("class", "choice_this");
    });
    //点击保存配送及支付方式
   /* $("#save_to_payment").click(function() {
        check_payment();
    })*/
    $(document).on("click","#save_to_payment",function() {
        check_payment();
    });
    //修改支付及配送方式
    $(document).on("click", "#payment_change", function() {
        $("#pay-ship-info,#save_to_payment,#address_text_save").show();
        $("#payment_ship_text,#payment_change,#address_change,#save_to_address").hide();
        $("#pay_ment").attr("class", "choice_this")
    });
    //点击保存收货人信息new_address_radio
    $(document).on("click", "#new_address_radio", function() {
        newAddress();
    });
    //选择已有的单选框按钮
    $(document).on('click', '.user_consignee_list', function() {
        $("#new_address_main,#save_address").hide();
        $("#set_address").show();
    });
    $(document).on('click', '#save_address', function() {
        save_consignee();
    });
    //点击保存 保存收货人信息
    $(document).on('click', '#save_to_address', function() {
        if ($("#new_address_radio").prop('checked')) {
            save_consignee();
        } else {
            setAddress();
        }
    });


    $("input:radio[name=inv_need_addr]").click(function() {
        if ($(this).val() == 0) {
            $("#receipt_address").hide();
        } else {
            $("#receipt_address").show();
        }
        invoiceNeedShipping();
    });
	
	 $("#onlinepay_btn").bind('click', function(e) {
        $("#onlinepay_btn form").submit();
    });
    $("#order_amount").bind('keydown', function(e) {
        if (e.keyCode < 48 || (e.keyCode > 57 && e.keyCode < 96) || (e.keyCode > 105 && e.keyCode < 112) || e.keyCode > 123) {

            switch (e.keyCode) {
                case 13:
                    e.keyCode = 9;
                case 8:
                case 9:
                case 10:
                case 17:
                case 18:
                case 20:
                case 33:
                case 34:
                case 35:
                case 36:
                case 37:
                case 38:
                case 39:
                case 40:
                case 45:
                case 46:
                case 91:
                case 92:
                case 93:
                case 127:
                case 144:
                    return true;
                default:
                    return false;
            }
        }
    });					   
						   
	 $("#tb_search").bind("keydown", function(e) {
        if (e.keyCode == 13 || e.which == 13 || e.charCode == 13) {
            search();
        }
    });
	 
    $("#btn_search").bind("click", search);
    Resize();
    $(window).resize(function() {

        Resize();
    })
    $("img.lazy").lazyload({
        threshold: 200
    });

    $(window).scroll(function() {
        if ($(window).scrollTop() > 121) {
            $(".hgs_nav_main").css({
                "position": "fixed",
                "top": 0 + "px"
            });
        } else {
            $(".hgs_nav_main").css({
                "position": ""
            });
        }
    })
    //搜索框默认
    $("#tb_search").val($("#default_search").text());
    $("#tb_search").click(function() {
        if ($(this).val() == $("#default_search").text()) {
            $(this).val("");
            $(this).css(
                "color", "#000"
            )
        }
    })

    // //邀请码
    // $(".invitation_system").click(function() {
    //     if ($(this).val() == "如有邀请码，请输入") {
    //         $(this).val("");
    //         $(".invitation_system").css(
    //             "background-color", "#fff"
    //         )
    //     }
    // });
    // $(".invitation_system").blur(function() {
    //     if ($(this).val() == "") {
    //         $(this).val("如有邀请码，请输入");
    //         $(".invitation_system").css(
    //             "background-color", "#F4F4F4"
    //         )
    //     }
    // });


    $(".index_product_main").mouseover(function() {
        var faheight = $(this).parent().height();
        $(this).parent().css("height", faheight + "px");
    })

    $("#tb_search").blur(function() {
        if ($(this).val() == "") {
            $(this).val($("#default_search").text());
            $(this).css(
                "color", "#ccc"
            )
        }
    })

    //ie6兼容导航，返回顶部代码
    if (r == "IE,6.0") { //ie6
        var firstheight = $(window).height() - 210;
        $(".sidepanel").css({
            "position": "absolute",
            "top": firstheight + "px"
        });
        $(window).scroll(function() {
            var ab = $(window).scrollTop();
            $(".sidepanel").css({
                "position": "absolute",
                "top": firstheight + ab + "px"
            });
            $(".top_center").css("padding-bottom", 36 + "px");
            if ($(window).scrollTop() > 121) {
                $(".hgs_nav_main").css({
                    "position": "absolute",
                    "top": ab + "px"
                });
                $(".sidepanel").css({
                    "position": "absolute",
                    "top": firstheight + ab - 45 + "px"
                });
            } else {
                $(".hgs_nav_main").css({
                    "position": "absolute",
                    "top": 121 + "px"
                });
            }
        });
    };

    $(".daily_check_in").click(function() {
        checkIn();
    })
    // $('.change_city_name span').text(function() {
    //   return $('.sitelist.selected').text();
    //});

    //微信扫一扫
    $(".wechat").mouseover(function() {
        $(".wechat_icon").show();
    }).mouseout(function() {
        $(".wechat_icon").hide();
    });

    $("#login_form").Validform({
        tiptype: 2,
        ajaxPost: true,
        callback: function(data) {
            signInResponse(data);
        }
    });

    $("#subscribe_form").Validform({
        btnSubmit: "#subscribe",
        tiptype: 4,
        ajaxPost: true,
        tipSweep: true,
        dragonfly: true,
        beforeSubmit: function(curform) {
            if ($("#subscribe_mail").val() == '') return false;
        },
        callback: function(data) {
            var tip = $("#subscribe_form").find('.Validform_checktip');
            if (data.code == 0) {
                tip.text('订阅成功');
            } else {
                tip.text('您已经订阅过,无需重复订阅');
            }
            setTimeout(function() {
                tip.text('');
            }, 3000);
        }
    });
    var registerForm = $("#register_form").Validform({
        tiptype: 2,
        ajaxPost: true,
        callback: function(data) {
            registerResponse(data);
        }
    });
    var forgetPasswordForm = $("#forget-password").Validform({
        tiptype: 2,
        ajaxPost: true,
        callback: function(data) {
            forgetPasswordResponse(data);
        }
    });
    var validateEmailForm = $("#validateEmail").Validform({
        tiptype: 4,
        ajaxPost: true,
        callback: function(data) {
            openDialog('验证邮箱', '邮件发送成功！请到您的邮箱里查收并激活后邮箱验证方可成功！', '确定', function() {
                if (data.code == 0) {
                    window.location.href = appUrl + "/Usercenter/userinfo";
                }
            });
        }
    });
    var validateMobileForm = $("#validateMobile").Validform({
        tiptype: 4,
        ajaxPost: true,
        callback: function(data) {

            openDialog('验证手机', data.msg, '确定', function() {
                if (data.code == 0) {
                    window.location.href = appUrl + "/Usercenter/userinfo";
                }
            });

        }
    });
    var cpFeedbackFrom = $("#feedback").Validform({
        tiptype: 4,
        ajaxPost: true,
        callback: function(data) {
            switch (data.code) {
                case 0:
                    openDialog('', "您的反馈已提交,我们会尽快处理");
                    cpFeedbackFrom.resetForm();
                    break;
                case -1:
                    openDialog('', "验证码错误");
                    break;
            }
            updateVerify();
        }

    });

    var cpOrderFrom = $("#cp-order").Validform({
        tiptype: 4,
        datatype: {
            "phone": function(gets, obj, curform, regxp) {
                var reg1 = regxp["m"],
                    reg2 = /(^(([0\+]\d{2,3}-)?(0\d{2,3})-)(\d{7,8})(-(\d{3,}))?$)|(^0{0,1}1[3|4|5|6|7|8|9][0-9]{9}$)/,
                    mobile = curform.find("#mobile");

                if (reg1.test(mobile.val())) {
                    return true;
                }
                if (reg2.test(gets)) {
                    return true;
                }

                return false;
            }
        },
        ajaxPost: true,
        callback: function(data) {
            switch (data.code) {
                case 0:
                    openDialog('提交成功', "您的采购需求已提交成功,我们会尽快联系您!");
                    cpOrderFrom.resetForm();
                    break;
                case -1:
                    openDialog('', "验证码错误");
                    break;
            }
            updateVerify();
        }

    });
    var commentForm = $("#commentForm").Validform({
        tiptype: 4,
        ajaxPost: true,
        callback: function(data) {
            switch (data.code) {
                case 0:
                    window.location.href = appUrl + '/Usercenter/commentList';
                    break;
                case -1:
                    openDialog('', "验证码错误");
                    break;
            }
            updateVerify();
        }

    });
    //lazyload
    $("img").lazyload({
        threshold: 300
    });
    $("img").lazyload({
        placeholder: "Js/lazyload/grey.gif",
        effect: "fadeIn"
    });
    //推荐商品加入购物车
    $(".need_login").click(function() {
        url = this.href;
        $('#signJumpPage').val(url);
        login();
        return false;
    })

    $(".a_style").click(function() {
        $(".product_tab").find('li').eq(1).click();
    });

    //根据轮播图数量加载按钮个数。
    var bannerNum = $(".banner_list a").size();
    var btnList = "";
    for (var i = 0; i < bannerNum; i++) {
        btnList = btnList + (i == 0 ? '<span class="hover"></span>' : '<span class=""></span>');
    }
    $(".lunbo_btn").append(btnList);
    $(".collect_hgs").mouseover(function() {
        $(".collect_hgs b").addClass("hover");
    }).mouseout(function() {
        $(".collect_hgs b").removeClass("hover");
    })
    $(".custom_service").mouseover(function() {
        var a = 'zhaoshou';
        $(".custom_service img").attr("src", appUrl + "/Tpl/Public/Images/" + a + ".gif");
    }).mouseleave(function() {
        var a = 'zhayan';
        $(".custom_service img").attr("src", appUrl + "/Tpl/Public/Images/" + a + ".gif");
    })

    $(".my_hgs").mouseover(function() {
        $(".my_hgs span").show();
        $(".my_hgs b").addClass("hover");
        $(".blank_box").show();
        $(".my_hgs_down").show();
    }).mouseout(function() {
        $(".my_hgs span").hide();
        $(".my_hgs b").removeClass("hover");
        $(".blank_box").hide();
        $(".my_hgs_down").hide();
    })

    $(".change_city_blank").mouseover(function() {
        $(".change_city_name").addClass("hover");
        $(".change_city_item").show();
    }).mouseout(function() {
        $(".change_city_name").removeClass("hover");
        $(".change_city_item").hide();
    })

    $(".micro_blog").mouseover(function() {
        $(this).children().show();
    }).mouseout(function() {
        $(this).children().hide();
    })

    //提示邮费信息选择
    //var cityName=$("#cityName").text();
    //if(cityName=="6"){
    //$("#postage_txt").text("深圳地区满99元免运费");
    //}else {
    //$("#postage_txt").text("购物满118元免运费");
    //}

    //选仓效果
    $(".storehouse_city").mouseover(function() {
        var storehouse = $(this).parent().parent().find(".storehouse_title").text();

        if (storehouse == "北京仓：") {
            $(".change_city_prompt img").attr("src", appUrl + "/Tpl/Public/Images/beijing_city.jpg")

        }
        if (storehouse == "深圳仓：") {
            $(".change_city_prompt img").attr("src", appUrl + "/Tpl/Public/Images/shenzhen_city.jpg")
        }
        if (storehouse == "成都仓：") {
            $(".change_city_prompt img").attr("src", appUrl + "/Tpl/Public/Images/chengdu_city.jpg")

        }
        if (storehouse == "上海仓：") {
            $(".change_city_prompt img").attr("src", appUrl + "/Tpl/Public/Images/shanghai_city.jpg")
        }
    })

    $(".storehouse_city").click(function() {
        var siteId = $(this).attr('siteId');
        var url = appUrl + "/Users/setSite/siteId/" + siteId;
        $.get(url, function() {
            location.reload();
        });
    })
    $(".change_city_name > span").text(function() {
        return $('.storehouse_city.hover').text();
    })


    //导航 
    $(".hgs_nav li").hover(function() {
        $(this).toggleClass("hover");
    })

    $(".hgs_nav li").click(function() {
        $(".hgs_nav li").removeClass("clicks");
        $(this).addClass("clicks");
    })

    //迷你购物车
    $("#cart_main").mouseover(function() {
        $("#mini_cart").attr("class", "mini_cart_hover");
        $(".minicart").show();
    }).mouseleave(function() {
        $("#mini_cart").attr("class", "mini_cart");
        $(".minicart").hide();
    })

    //个人中心左导航
    $(".user_item_title").click(function() {
        $(this).siblings().toggle();
        $(this).toggleClass("user_item_title_click");
    })
    //个人中心跟踪包裹
    $(".follow_package_main").hover(function() {
        $(".follow_package_detailed", this).toggle();
        $(".follow_package_blank", this).toggle();
        $('.follow_package', this).toggleClass("follow_package_click");
    })

    //评论星星
    $(".write_conment_img_btn").each(function(i) {
        var y = i + 1;
        $(this).click(function() {
            $("#conment_bgimg").attr("class", "write_conment_bgimg_" + y);
            $("#rank").val(y);
        })
    })

    //tab
    $(".affiliate-tab").children().hide();
    $(".affiliate-tab").children().eq(0).show();
    $(".js-tab-control").each(function(i) {
        $(this).click(function() {
            if (!$(this).hasClass("hover")) {
                $(this).addClass("hover").siblings().removeClass("hover");
                $(".affiliate-tab").children().eq(i).show().siblings().hide();
            }
        })
    })
    //flow 优惠三部曲显示弹窗
    $(".toggle_mouseover").each(function(i) {
        var y = i + 1;
        $(this).click(function() {
            $(".toggle_title_img", this).toggleClass("toggle_title_img_hover");
            if (y == 1) {
                $("#discount_main").toggle();
            }
            if (y == 2) {
                $("#integral_main").toggle();
            }
            if (y == 3) {
                $("#receipt_main").toggle();
            }
        })
    })
    //flow 礼品卡优惠劵tab
    $("[name=discount_tab]").each(function(i) {
        var y = i + 1;
        $(this).click(function() {
            $("[name=discount_tab]").attr("class", "discount_tab");
            $(this).attr("class", "discount_tab_click");
            $(".discount_main").hide();
            $("#discount_main_" + y).show();
        })
    })

    //判断配送区域
    $("#selDisctricts").change(function() {
        var checkText = $("#selDisctricts").find("option:selected").text();
        if (checkText == "大明湖") {
            alert("将在两个小时内送达");
        }
    });

    //发票 单选框
    $("#receipt_yes").click(function() {
        $("#receipt_pack").show();

    })

    $("#receipt_no").click(function() {
        $("#receipt_address_no").prop('checked', true).click();
        $("#receipt_pack").hide();
    })

    $("#receipt_address_yes").click(function() {
        $("#receipt_address").show();
    })


    $("#receipt_address_no").click(function() {
        $("#receipt_address").hide();
    })

    //商品详情配送地址
    $(".deliver_item_bottom li").each(function(i) {
        $(this).click(function() {
            goods_address_tab(i);
            $(".area_list").children().hide();
            $(".area_list").children().eq(i).show();
        })
    })

    function goods_address_tab(i) {
        $(".deliver_item_bottom li").attr("class", "deliver_item_bottom_li");
        $(".deliver_item_bottom li").eq(i).attr("class", "deliver_item_bottom_li_hover");
    }
    $("#gotopbtn").hide();
    //当滚动条的位置处于距顶部121像素以下时，跳转链接出现，否则消失

    $(window).scroll(function() {
        if ($(window).scrollTop() > 121) {
            $("#gotopbtn").show();
        } else {
            $("#gotopbtn").hide();
        }
    });
    //当点击跳转链接后，回到页面顶部位置
    $("#gotopbtn").click(function() {
        $('body,html').animate({
            scrollTop: 0
        }, 300);
        return false;
    });

    // 商品详情页的省市区三级联动
    $(document).on('click', '.province', function() {

        $(".area_list").children().hide();
        $(".area_list").children().eq(1).show();
        goods_address_tab(1);
        var prov_id = $(this).attr('id');
        var prov_name = $(this).text();
        $("#province_id").val(prov_id);
        // 刷新省标题
        $("#user_province").text(prov_name);
        $.get(appUrl + "/Product/ajaxCityList?rid=" + prov_id, function(res) {
            $("#city_list").html(res);
            $("#district_list").html('');
            $('#user_city').html('请选择市');
            $('#user_district').html('请选择区');
            $('#district_id').val('');
        }, 'JSON');
    });
    $(document).on('click', '.city', function() {
        $(".area_list").children().hide();
        $(".area_list").children().eq(2).show();
        goods_address_tab(2);
        var city_id = $(this).attr('id');
        var city_name = $(this).text();
        // 刷新市标题
        $("#user_city").text(city_name);
        $("#city_id").val(city_id);
        $.get(appUrl + "/Product/ajaxDistrictList?rid=" + city_id, function(res) {
            $("#district_list").html(res);
            $("#user_district").click();
        }, 'JSON');
    });
    $(document).on('click', '.district', function() {

        $(".deliver_address_item").hide();
        $(".deliver_address_box_hover").attr("class", "deliver_address_box");
        var district_id = $(this).attr('id');
        var district_name = $(this).text();
        // 刷新区标题
        $("#user_district").text(district_name);
        // 刷新总标题
        var prov_name = $('#user_province').text();
        var city_name = $('#user_city').text();
        var dest_name = prov_name + city_name + district_name;
        $('#user_dest').text(dest_name);
        $("#district_id").val(district_id);

        $.get(appUrl + "/Product/saveUserAddressSelection?prov=" + $("#province_id").val() + "&city=" + $("#city_id").val() + "&district=" + $("#district_id").val(),
            function(pname) {
                $('#cityName').text(pname);
                $('div.storehouse_city.hover').removeClass('hover');
                $('div.storehouse_city:contains(' + pname + ')').addClass('hover');
                //TODO 换全国地图
            });

    });


    $(".deliver_address_left").mouseover(function() {
        $(this).children().eq(0).attr("class", "deliver_address_box_hover");
        $(this).children().eq(1).show();
    })
    //配送区域关闭按钮。
    $(".deliver_address_item_close").click(function() {
        $(".deliver_address_left").children().eq(0).attr("class", "deliver_address_box");
        $(".deliver_address_item").hide();
    })
	
	$(document).bind("click",function(e){
		  var target  = $(e.target);
		  if(target.closest(".deliver_address_item").length == 0){
        		$(".deliver_address_left").children().eq(0).attr("class", "deliver_address_box");
			   	$(".deliver_address_item").hide();
		  }
	 })

    //商品数量加减
    //+号按钮
    $(".product_num_add").click(function() {
        var num = parseInt($("#product_num").val()) + 1;
        num = num > 100 ? 100 : num;
        $("#product_num").val(num);
    })
    //-号按钮
    $(".product_num_del").click(function() {
        var num = parseInt($("#product_num").val()) - 1;
        num = num < 1 ? 1 : num;
        $("#product_num").val(num);
    })


    $("#product_num").keyup(function() {
        var num = parseInt($("#product_num").val());
        if (isNaN(num)) {
            $("#product_num").val(1);
        } else {
            if (num > 100 || num < 1) {
                $("#product_num").val(1);
            } else {
                $("#product_num").val(num);
            };
        };
    });



    $("#js_product_tab").children().hide();
    $("#js_product_tab").children().eq(0).show();
    $(".product_tab li").each(function(i) {
        $(this).click(function() {
            $(".product_tab li").removeClass("hover");
            $(this).addClass("hover");
            $("#js_product_tab").children().hide();
            $("#js_product_tab").children().eq(i).show();
        })
    })
    //登录注册弹窗
    $(".login_register_btn").click(function() {
        $("#login_main").hide();
        $("#register_main").show();
    })

    $(".forget_pass").click(function() {
        $("#login_main").hide();
        $("#find_pass").show();
    })

    $(".register_login_btn").click(function() {
        $("#login_main").show();
        $("#register_main").hide();
    })

    $(".pop_title img").click(function() {
        $(".pop_main").hide();
        $("#bg").remove();
    })

    // // 关闭提示弹窗
    // $(".pop_btn").click(function() {
    //     $(".pop_main").hide();
    //     $("#bg").remove();
    // })
    //订阅邮箱提示
    $("#subscribe_mail").click(function() {
        if ($(this).val() == "请输入订阅邮箱") {
            $(this).val("");
        }
    })
    $("#subscribe_mail").blur(function() {
        if ($(this).val() == "") {
            $(this).val("请输入订阅邮箱");
        }
    })

    //商品详情二维码
    $(".sweep_icon").mouseover(function() {
        $(".sweep_big_img").show();
        $(".sweep_prompt").addClass("hover");
    }).mouseout(function() {
        $(".sweep_big_img").hide();

        $(".sweep_prompt").removeClass("hover");
    });
    $(".sendValidateCode").click(function() {
        mobile = $("#validMobile").val();
        sendValidateCode(mobile);
    })

});

//加入购物车效果
function addcart(imgsrc, x, y, callback, callback_param) {
    $("#floatOrder").remove();
    $('body').append('<div id="floatOrder"><img src="" width="36" height="36" /></div');
    $("#floatOrder").find("img").attr("src", "" + imgsrc + "");
    var X = $("#mini_cart").offset().left;
    var Y = $("#mini_cart").offset().top;
    $("#floatOrder").show();
    $("#floatOrder").css({
        'left': x,
        'top': y
    }).animate({
        'left': X + 20,
        'top': Y + 50
    }, 500, function() {
        $("#floatOrder").animate({
            'left': X + 20,
            'top': Y
        }, 200, function() {
            $("#floatOrder").fadeOut();
            callback(callback_param);
        });
    });
}
//弹窗页面

function Popshow(divId) {
    bodybg(395, 185);
    $(divId).show();
}

function openDialog(title, msg, closeText, closeCallback, confirmText, confirmCallback) {
    bodybg(395, 185);
    if (title == '') {
        title = '提示'
    };
    if (!closeText) closeText = '确定';
    var closeBtn = $("#dlg-close");
    closeBtn.text(closeText).one('click', function() {
        if (closeCallback && typeof(closeCallback) == 'function') {
            closeCallback();
        }
        closeDialog();
    });

    if (confirmText) {
        var confirmBtn = $("<div></div>").attr('id', 'dlg-confirm').addClass('btn_style_1 pop_btn').text(confirmText);
        confirmBtn.one('click', function() {
            if (confirmCallback && typeof(confirmCallback) == 'function') {
                confirmCallback();
            }
            closeDialog();
        });
    }
    $("#dlg-close").after(confirmBtn);
    $('#prompt_title').text(title);
    $('#prompt_msg_msg').text(msg);
    $('#prompt_msg').show();

}

function sendValidateCode(mobile) {
    postdata = {
        data: mobile
    }
    $.post(appUrl + '/Usercenter/sendValidateCode', postdata, function(result) {

    }, 'JSON').success(function(result) {
        openDialog('发送验证玛', result.msg);
    });
}

function checkIn() {
    var url = appUrl + '/Usercenter/checkin';
    $.get(url, function(result) {
        if (result.code == 0) result.msg = '签到成功';
        openDialog('', result.msg);
    }, 'JSON');
}

function bodybg(Widths, Heights) {
    $aheight = $(document).height();
    $awidth = $(document).width();
    $docu = "<div id=\"bg\" style=\"opacity:0.7!important;filter:progid:DXImageTransform.Microsoft.Alpha(Opacity=70)!important;height:" + $aheight + "px;width:100%;max-width:120000px;position:absolute;left:0px;top:0px;background:#000;z-index:99;min-width:1200px;\"></div>";
    $("body").append($docu);


    aOffsetLeft = ($(window).width() / 2) - (parseInt(Widths) / 2);
    aOffsetTop = ($(window).height() / 2) - (parseInt(Heights) / 2);
    $(".login_register_main").css({
        "left": aOffsetLeft + "px",
        "top": aOffsetTop + "px"
    });
    $(".pop_main").css({
        "left": aOffsetLeft + "px",
        "top": aOffsetTop + "px"
    });
    if (r == "IE,6.0") { //ie6
        $(window).scroll(function() {
            var aa = $(window).scrollTop() + aOffsetTop;
            $(".login_register_main").css({
                "left": aOffsetLeft + "px",
                "top": aa + "px",
                position: "absolute"
            });
            $(".pop_main").css({
                "left": aOffsetLeft + "px",
                "top": aa + "px",
                position: "absolute"
            });
        })

        $(".login_register_main").css({
            "left": aOffsetLeft + "px",
            "top": aOffsetTop + "px",
            position: "absolute"
        });
        $(".pop_main").css({
            "left": aOffsetLeft + "px",
            "top": aOffsetTop + "px",
            position: "absolute"
        });
    }
    $(window).resize(function() {
        aOffsetLeft = ($(window).width() / 2) - (parseInt(Widths) / 2);
        aOffsetTop = ($(window).height() / 2) - (parseInt(Heights) / 2);
        $(".login_register_main").css({
            "left": aOffsetLeft + "px",
            "top": aOffsetTop + "px"
        });
        $(".pop_main").css({
            "left": aOffsetLeft + "px",
            "top": aOffsetTop + "px"
        });
    });

}

function login() {
    bodybg(570, 380);
    $(".pop_main").hide();
    $("#login_main").show();
    $(".login_register_main").show();
}

function register() {
    bodybg(570, 380);
    $(".pop_main").hide();
    $("#register_main").show();
    $(".login_register_main").show();
}

function closelore_main() {
    $(".login_register_main").hide();
    $(".login_register_main").children().not(":first").hide();
    $("#bg").remove();
}

function Resize() {
    var winWidth = parseInt($(window).width());
    if (winWidth > 1190) {
        $("#change_css").attr("class", "change_1190");
    } else {
        $("#change_css").attr("class", "");
    }
}

//客服弹窗  
function ShowDialog() {
    var url = "http://qiao.baidu.com/v3/?module=default&controller=webim&action=index&siteid=3058791";
    var iWidth = 780; //窗口宽度         
    var iHeight = 550; //窗口高度          
    var iTop = (window.screen.height - iHeight) / 2 - 50;
    var iLeft = (window.screen.width - iWidth) / 2;
    window.open(url, "Detail", "Scrollbars=no,Toolbar=no,Location=no,Direction=no,Resizeable=no,Width=" + iWidth + " ,Height=" + iHeight + ",top=" + iTop + ",left=" + iLeft);
}

function forgetPasswordResponse(res) {
    var forgetTip = $(".forget-tip");
    forgetTip.html(res.msg);
    if (res.code == -1 && forgetTip.hasClass('Validform_wrong') == false) {
        forgetTip.addClass('Validform_wrong')
    } else if (res.code == 0) {
        forgetTip.removeClass('Validform_wrong');
    }
}

function closeDialog() {
    $(".pop_main").hide();
    $("#bg").remove();
    $("#dlg-confirm").remove();
}


function browser() {
    var ua = window.navigator.userAgent,
        ret = "";
    if (/Firefox/g.test(ua)) {
        ua = ua.split(" ");
        ret = "Firefox|" + ua[ua.length - 1].split("/")[1];
    } else if (/MSIE/g.test(ua)) {
        ua = ua.split(";");
        ret = "IE|" + ua[1].split(" ")[2];
    } else if (/Opera/g.test(ua)) {
        ua = ua.split(" ");
        ret = "Opera|" + ua[ua.length - 1].split("/")[1];
    } else if (/Chrome/g.test(ua)) {
        ua = ua.split(" ");
        ret = "Chrome|" + ua[ua.length - 2].split("/")[1];
    } else if (/^apple\s+/i.test(navigator.vendor)) {
        ua = ua.split(" ");
        ret = "Safair|" + ua[ua.length - 2].split("/")[1];
    } else {
        ret = "未知浏览器";
    }
    return ret.split("|");
}

function search() {
    searchname = $("#tb_search").val();
    if (searchname == null || searchname == '') {
        openDialog('提示', '搜索关键词不能为空');
        return;
    }


    url = appUrl + "/Search/index/searchname/" + searchname;
    window.location.href = url;
}


// 确认充值订单表单提交
function confirmRecharge() {
    order_amount = $("#order_amount").val();
    if (order_amount < 10 || order_amount > 50000) {
        openDialog('提示', '只能填写大于等于10，小于等于50000的整数金额');
        return;
    }

    $("#rechargeform").submit();
}

/**
 * 获取城市列表
 */
function loadCities() {
    var provinceId = $("#selProvince").find("option:selected").val();
    var provinceName = $("#selProvince").find("option:selected").text();
    $("#selDistricts").hide();
    $.get(appUrl + "/Flow/ajaxCityList?rid=" + provinceId,
        function(res) {
            $("#selCity").html(res);
            $("#selCity").show();
            if ($("#selCity > option").length == 1) {
                loadDistricts();
            }
        }, 'JSON');
}


/**
 * 获取城区列表
 */
function loadDistricts() {
    var cityId = $("#selCity").find("option:selected").val();
    var cityName = $("#selCity").find("option:selected").text();
    $.get(appUrl + "/Flow/ajaxDistrictList?rid=" + cityId,
        function(res) {
            $("#selDistricts").html(res);
        }, 'JSON');
    $("#selDistricts").show();

}

/**
 * 获取发票单独寄送部分的城市列表
 */
function loadCities2() {
    var provinceId = $("#selProvince2").find("option:selected").val();
    var provinceName = $("#selProvince2").find("option:selected").text();
    $.get(appUrl + "/Flow/ajaxCityList?rid=" + provinceId,
        function(res) {
            $("#selCity2").html(res);
            if ($("#selCity2 > option").length == 1) {
                loadDistricts2();
            }
        }, 'JSON');
}


/**
 * 获取发票单独寄送部分的城区列表
 */
function loadDistricts2() {
    var cityId = $("#selCity2").find("option:selected").val();
    var cityName = $("#selCity2").find("option:selected").text();
    $.get(appUrl + "/Flow/ajaxDistrictList?rid=" + cityId,
        function(res) {
            $("#selDistricts2").html(res);
        }, 'JSON');
}


function getPrdNum() {
    return $("#product_num").val();
}


function closeTab(id) {
    $("#" + id).hide();
}

//添加商品到购物车
function addToCart(ele) {
    var pid = $(ele).attr("data-pid");
    var prdNum = parseInt(arguments[1] ? arguments[1] : 1);
    var oldprdNum = parseInt($(".prd_num_" + pid).val());

    if (oldprdNum + prdNum > 99) {
        openDialog('', "单个商品数量不能超过100");
        return;
    }


    var product = {
        goods_number: prdNum,
        pid: pid
    };

    $.post(appUrl + '/Cart/addTocart', product, function(result) {
        if (result.msg == "success") {
            var picsrc = $("#picsrc_" + pid).attr('src');
            if (picsrc != null && picsrc != '') {
                var x = $(ele).offset().left;
                var y = $(ele).offset().top;
                addcart(picsrc, x, y, addtocart_response, result);
            } else {
                addtocart_response(result);
            }
        } else {
            openDialog('提示', '购物车内已经有啦，再抢店家就赔啦');
        }
    }, 'JSON');
}


function addtocart_response(result) {
    $("#cart_main").html(result.cart_list);
    $(".left span").html(result.countPrd);
    $(".minicart_num").html(result.countPrd);
    $(".right span").html("￥" + result.cartTotal);

}

//从购物车删除商品
function delCart(pid) {

    $.post(appUrl + '/Cart/removePrd', 'pid=' + pid, function(result) {
        delete_cartresponse(result);
    }, 'JSON');
}

function delete_cartresponse(result) {
    if (result.msg == "success") {
        $("#cart_main").html(result.cart_list);
        $("#cartconnect").html(result.big_cart_list);
        $(".left span").html(result.countPrd);
        $(".minicart_num").html(result.countPrd);
        $(".right span").html("￥" + result.cartTotal);
        $("#cartfee").html("￥" + result.cartTotal);
        $("#credit").html(parseInt(result.cartTotal));
        $(".minicart").show();
    }

}

function min_intval_filter(goods_number) {
    if (isNaN(goods_number)) {
        goods_number = 1;
    }
    goods_number = parseInt(Math.ceil(goods_number));
    if (goods_number < 1) {
        goods_number = 1;
    } else if (goods_number > 100) {
        goods_number = 100
    }
    return goods_number;
}

//+-改变购物车中的数量
function changeCartNum(rec_id, diff) {
    //openDialog('','0');
    var min_prd_number = parseInt($('#min_goods_number_' + rec_id).val());
    min_prd_number = min_intval_filter(min_prd_number);

    //openDialog('','1 min_prd_number=' + min_prd_number);
    min_prd_number = min_prd_number + diff;
    //	openDialog('','2 min_prd_number=' + min_prd_number);
    if (min_prd_number < 1) {
        //openDialog('','ok');
        pid = $("#min_goods_number_" + rec_id).attr("data-pid");
        delCart(pid);
    } else if (min_prd_number > 100) {
        return;
    } else {
        //$.post('Cart/modifyPrdNum', 'rec_id=' + rec_id +'&goods_number=' + min_prd_number, min_change_prd_number_response,'JSON');                
        $.post(appUrl + '/Cart/modifyPrdNum', 'rec_id=' + rec_id + '&goods_number=' + min_prd_number, function(result) {
            min_change_prd_number_response(result);
        }, 'JSON');
    }
    //  min_change_prd_number(rec_id, min_prd_number);

}


function min_change_prd_number(rec_id, min_prd_number) {

    min_prd_number = min_intval_filter(min_prd_number);
    // $(".bigcart_num").val(min_prd_number);
    //openDialog('','4 min_prd_number=' + min_prd_number);
    $.post(appUrl + '/Cart/modifyPrdNum', 'rec_id=' + rec_id + '&goods_number=' + min_prd_number, function(result) {
        min_change_prd_number_response(result);
    }, 'JSON');

}

function min_change_prd_number_response(result) {


    if (result.msg == "success") {
        // openDialog('',"sd");
        $("#cart_main").html(result.cart_list);
        $("#cartconnect").html(result.big_cart_list);
        $(".left span").html(result.countPrd);
        $(".minicart_num").html(result.countPrd);
        $(".right span").html("￥" + result.cartTotal);
        $("#cartfee").html("￥" + result.cartTotal);
        $("#credit").html(parseInt(result.cartTotal));
        $(".minicart").show();


    }

}


//------------ 结算页-------------//

//增加新地址
function save_consignee() {
    var data = {
        act: 'add',
        adr_id: $("#adr_id").val(),
        consignee: $("#consignee").val(),
        province: $("#selProvince").val(),
        city: $("#selCity").val(),
        district: $("#selDistricts").val(),
        address: $("#address").val(),
        mobile: $("#mobilephone").val()
    }

    var reg = /^([\w\u4e00-\u9fa5]{1,20})$/g;
    if (data.consignee == '') {
        openDialog('', "收货人姓名不能为空")
        return;
    }

    if (reg.test(data.consignee) == false) {
        openDialog('', '收货人的格式不正确');
        return;
    }

    if (data.province == 0) {
        openDialog('', '请选择城市');
        return;
    }
    if (data.city == 0) {
        openDialog('', '请选择省份');
        return;
    }
    if (data.district == 0) {
        openDialog('', '请选择区域');
        return;
    }


    if (data.address == '') {
        openDialog('', '收货地址不能为空');
        return;
    }

    if (data.mobile == '') {
        openDialog('', '手机号不能为空');
        return;
    }

    var reg = /^1[3458]\d{9}$/g; //手机号码的验证 11位，
    if (reg.test(data.mobile) == false) {

        openDialog('', '手机的格式不正确');
        return;
    }
    if ($("#selDistricts").is(":hidden")) {
        openDialog('', "请选择区域");
        return;
    }

    $.post(appUrl + '/Flow/consigneeOperateInfo', data, function(res) {
        add_consignee_response(res);
    }, 'JSON');


}


function add_consignee_response(res) {
    if (res.msg == "success") {
        $("#hgs_consignee").html(res.consignee_list);
        $("#pay_ment").html(result.paynship);
        setShippingTime(result.timestamp);
        $("#consignee_list_radio,#save_to_address,#payment_ship_text,#save_conignee_before").hide();
        $("#address_change,#address_abstract,#pay-ship-info,#save_to_payment").show();
        $("#pay_ment").attr("class", "choice_this");
        $("#hgs_consignee").attr("class", "checkout_box");
    }

}




function delete_consignee(adr_id) {

    $.post(appUrl + '/Flow/consigneeOperateInfo', 'adr_id=' + adr_id + '&act=drop', function(result) {
        delete_consignee_response(result);
    }, 'JSON');

}

function delete_consignee_response(result) {
    if (result.msg == "success") {
        $("#hgs_consignee").html(result.consignee_list);
    }

}

function update_consignee(adr_id) {

    $(".consignee_" + adr_id).prop("checked", true);
    var data = {
        act: 'update',
        adr_id: adr_id,
        consignee: $("#consignee").val(),
        province: $("#selProvince").val(),
        city: $("#selCity").val(),
        district: $("#selDistricts").val(),
        address: $("#address").val(),
        mobile: $("#mobilephone").val()
    }
    $.post(appUrl + '/Flow/consigneeOperateInfo', data, function(result) {
        update_consignee_response(result);
    }, 'JSON');

}

function update_consignee_response(result) {
    $("#hgs_consignee").html(result.consignee_list);
    $("#new_address_main,#save_address,#selDistricts").show();
    //$("#hgs_consignee").removeClass("class","checkout_box");
    $("#hgs_consignee").attr("class", "choice_this");
    $("#set_address").hide();
}

function setAddress() {
    id = $(".user_consignee_list:checked").val();
    setSelectedAddress(id);
}

//确认选择的地址
function setSelectedAddress(addressId) {

    address_absctract = $("#address_" + addressId).val();
    $("#address_abstract").text(address_absctract).show();
    $("#consignee_list_radio,#save_to_address,#save_conignee_before,#payment_ship_text").hide();
    //$("#address_text_save,#pay-ship-info,#save_to_payment").show();
    //$("#pay_ment").attr("class", "choice_this");
    $("#hgs_consignee").attr("class", "checkout_box");
    $.post(appUrl + '/Flow/consigneeOperateInfo', 'adr_id=' + addressId + '&act=update', function(result) {
        set_consignee_response(result);
    }, 'JSON');
}

function set_consignee_response(result) {
    if (result.msg == "success") {
        updateFeeSummary(result);
        $("#pay_ment").html(result.paynship);
        setShippingTime(result.timestamp);
        $("#payment_ship_text").hide();
        $("#address_text_save,#pay-ship-info,#save_to_payment").show();
        $("#pay_ment").attr("class", "choice_this");
        $("#hgs_consignee").attr("class", "checkout_box");
         $("#save_conignee_before").hide();
    }
}

function updateFeeSummary(result) {
    $("#goods-fee").text('￥' + result.goods);
    $("#shipping-fee").text('￥' + result.shipping);
    $("#invoice-fee").text('￥' + result.invoice);
    $("#bonus-deduct").text('￥' + result.bonus);
    $("#card-deduct").text('￥' + result.giftcard);
    $("#credit-deduct").text('￥' + result.credit);
    $("#amount_formated").text('￥' + result.amount)
}

function setShippingTime(timestamp) {
    timestamp = parseInt(timestamp);
    var tday = (timestamp + 86400) * 1000;
    var tmr = (timestamp + 86400 * 2) * 1000;
    var dat = (timestamp + 86400 * 3) * 1000;
    var dd = new Date(tday);
    var h = dd.getHours();
    dd.getDate();
    var y = dd.getFullYear() + "-";
    var m = dd.getMonth() + 1 + "-";
    var d = dd.getDate() + "（明天）";
    var tod = new Date(tmr);
    var y1 = tod.getFullYear() + "-";
    var m1 = tod.getMonth() + 1 + "-";
    var d1 = tod.getDate() + "（后天）";
    var dot = new Date(dat)
    var y2 = dot.getFullYear() + "-";
    var m2 = dot.getMonth() + 1 + "-";
    var d2 = dot.getDate() + "（大后天）";
    $("#time_one_am").text(y + m + d + "09:00-18:00");
    $("#time_one_pm").text(y + m + d + "18:00-22:00");
    $("#time_two_am").text(y1 + m1 + d1 + "09:00-18:00");
    $("#time_two_pm").text(y1 + m1 + d1 + "18:00-22:00");
    $("#time_three_am").text(y2 + m2 + d2 + "09:00-18:00");
    $("#time_three_pm").text(y2 + m2 + d2 + "18:00-22:00");

    if (h > 22) {
        $("#time_one_am").hide();
    } else {
        $("#time_one_am").show();
    }
}

function check_payment() {
    var payment = $('input[name="payment"]:checked').val();

    if (payment >= 1 || payment.length > 2) {

        if (payment == 1) {
            paymentText = '货到付款';
            var times_text = $("#times_list").find("option:selected").text();

        } else if (payment == 2) {
            paymentText = '支付宝';
            var times_text = $("#times_list option:selected").text();

        } else {
            paymentText = '网上银行在线支付';
            var times_text = $("#times_list").find("option:selected").text();
        }
        var shipping = $('input[name="shipping_id"]:checked').attr("sname");
        //alert(shipping);
        if (shipping == "顺丰快递") {
            shippingText = shipping;
        } else {
            if (times_text == "任意时间") {
                shippingText = "花果山物流默认时间配送";
            } else {
                shippingText = "花果山物流将于以下时间为您配送：" + times_text;
            }
        }
        $("#ship_text").text(shippingText).show();
        $("#pay-ship-info,#save_to_payment,#address_text_save,#invoiceInfoTexignee_before").hide();
        $("#payment_ship_text,#payment_change,#address_change").show();
        $("#payment_text").text(paymentText).show();

    }
    $("#pay_ment").attr("class", "checkout_box");
    $("#address_text_save,#save_conignee_before").hide();
    $("#address_change").show();
}

function re_comment(id) {

    divid = "recomment_form_" + id;
    if ($(".need_login").size() > 0) {
        return false;
    }
    $("[data-id=" + divid + "]").toggle();
}

function selectBonus(val) {
    var postdata = {
        bonus_id: val
    }
    $.post(appUrl + "/Flow/selectBonus", postdata, function(result) {
        dealDeductInfo(result);
        updateFeeSummary(result);
    }, 'JSON');
}

function dealDeductInfo(result) {
    var bcText = pointText = "";
    if (parseInt(result.bonus) > 0) {
        bcText = '使用优惠券抵扣:￥' + result.bonus;
    }
    if (parseInt(result.giftcard) > 0) {
        bcText = bcText + ' 使用礼品卡抵扣:￥' + result.giftcard;
    }
    if (result.usePoint > 0) {
        pointText = '使用 ' + result.usePoint + ' 积分抵消￥' + result.credit;
    }
    $("#bc-deduct").text(bcText);
    $('#integralAmount').text(pointText);

}

function goodsRecomment(frm) {
    var cmt = new Object;
    cmt.re_username = $(frm).children("#re_username").val();
    cmt.content = $(frm).children("#content").val();
    cmt.parent_id = $(frm).children("#parent_id").val();
    cmt.uid = $(frm).children("#uid").val();
    cmt.username = $(frm).children("#username").val();
    cmt.gid = $(frm).children("#gid").val();
    //    openDialog('',cmt.parent_id);
    // if (cmt.content.length == 0)
    // {
    //    $("#tips_big_div").show();
    //    $("#tips_word").html("评论内容不能为空。");
    //    return false;
    // }
    // openDialog('','goodsRecomment re_username' + cmt.re_username + ' parent_id' + cmt.parent_id);
    // Ajax.call('comment.php', 'act=recomment&cmt=' + $.toJSON(cmt), goodsRecommentResponse, 'POST', 'JSON');
    // return false;

    $.post(appUrl + "/Product/reComment", {
            re_username: cmt.re_username,
            parent_id: cmt.parent_id,
            content: cmt.content,
            uid: cmt.uid,
            username: cmt.username,
            gid: cmt.gid
        },
        function(res) {
            goodsRecommentResponse(res);
        }, 'JSON');

}

/**
 * wwz edit 商品详情页回复评论
 */
function goodsRecommentResponse(result) {
    if (result.msg == "success") {
        $("[name=content]").val("");
        $("#product_comment_list").html(result.body);
        $("#product_comment_list2").html(result.body);
        $(".product_tab li")[1].click();
    }
}




//对发票系列的输入框进行正则验证

function checke_invoice() {

    var need_invoice = $('input[name="need_invoice"]:checked').val();
    var need_addr = $('input[name="inv_need_addr"]:checked').val();
    var inv_type = $('input[name="inv_type"]:checked').val();
    var inv_payee = $.trim($("#inv_payee").val());
    var inv_content = $("#inv_content").find("option:selected").text();
    var inv_username = $.trim($("#inv_consignee").val());
    var selProvincess = $("#selProvincess").find("option:selected").val();
    var selCitiess = $("#selCitiess").find("option:selected").val();
    var selDisctrictss = $("#selDisctrictss").find("option:selected").val();
    var inv_address = $.trim($("#inv_address").val());
    var inv_phone = $.trim($("#inv_phone").val());
    var invoice_text = "不需要发票";
    if (need_invoice == 1) { //如果需要发票

        if (inv_payee != '') { //如果发票抬头不为空
            var reg = /^([\w\(\)\（\）u4e00-\u9fa5]{1,200})$/g; //发票抬头,
            if (reg.test(inv_payee) == false) {
                openDialog('', '发票格式不正确');
                return;
            }
            invoice_text = "发票抬头：" + inv_payee;
        } else {

            openDialog('', '发票抬头不能为空');
            return;

        }
        if (need_addr == 1) { //如果需要寄送发票
            invoice_text += " 发票另外寄送，加收￥10";
            if (inv_username != '') {

                var reg = /^([\w\u4e00-\u9fa5]{1,20})$/g;

                if (reg.test(inv_username) == false) {
                    openDialog('', '发票收货人姓名的格式不正确');
                    return;
                }
            } else {

                openDialog('', '发票收货人姓名不能为空');
                return;
            }

            /*if (selProvincess == 0) {
                openDialog('', '请选择省份');
                return;
            }
            if (selCitiess == 0) {
                openDialog('', '请选择城市');
                return;

            }
            if (selDisctrictss == 0) {
                openDialog('', '请选择区域');
                return;
            }*/
            if (inv_address == '') {
                openDialog('', '收货地址不能为空');
                return;
            }
            if (inv_phone != '') {
                var reg = /^1[3458]\d{9}$/g; //手机号码的验证 11位，
                if (reg.test(inv_phone) == false) {

                    openDialog('', '手机的格式不正确');
                    return;
                }

            } else {

                openDialog('', '手机号码不能为空');
                return;

            }
        }
    }

    $("#invoiceInfoText").text(invoice_text).show();
    $("#receipt_main").hide();
    $("#receipt_id").removeClass("toggle_title_img_hover");

}

//使用积分

function change_integral() {
    var integral_use_most = $("#integral_use_most").text();
    var integral = $('#integral').val();
    if (integral != '') {
        var reg = /^\d+$/g;
        if (reg.test(integral) == false) {
            $('#integral').val(0);
            $("#integralAmount").text('');
            openDialog('', "积分只能为数字");
            return;
        } else if (integral % 100 != 0) {
            $('#integral').val(0);
            //openDialog('',"积分只能是100的倍数");
        } else if (integral == 0) {
            $("#integral_main").hide();
            $("#integral_img").removeClass("toggle_title_img_hover");
        } else if (integral > integral_use_most) {
            $('#integral').val(0);
            $("#integralAmount").text('');
            return;
        }
    } else {
        openDialog('', '积分不能为空');
    }
    var postdata = {
        pay_point: integral
    }
    $.post(appUrl + '/Flow/useCredit', postdata, function(result) {
        change_integral_response(result);
    }, 'JSON');


}

function change_integral_response(result) {
    if (result.msg == "success") {
        dealDeductInfo(result);
        updateFeeSummary(result);
        $("#integral_main").hide();
        $("#integral_img").removeClass("toggle_title_img_hover");
    } else {
        openDialog('', result.msg);
        return false;
    }
}

function invoiceNeedShipping() {

    var val = $('#receipt_address_yes:checked').val();
    val = parseInt(val);
    $.post(appUrl + '/Flow/invoiceNeedShipping', 'needvoice=' + val, function(result) {
        updateFeeSummary(result);
    }, 'JSON');

}

//提交订单验证
function Validform() {
    var openTab = $(".choice_this");
    if (openTab.length > 0) {
        openDialog('','清先确认订单配送支付信息');
        return false;
    }
    var extTab = $('.toggle_title_img_hover');
    if (extTab.length > 0) {
        openDialog('','清先确认订单优惠及发票信息');
        return false;
    }    

    return true;
}

function newAddress() {
    $("#adr_id").val(0);
    $("#consignee,#address,#mobile").val('');
    $("#new_address_main,#save_address").show();
    $("#set_address").hide();
}


function password_format_error_msg() {
    openDialog('', "密码格式错误，密码太长或太短");
}


function save_user_address() {
    // 获取省市区
    var prov_id = $('#provinces').children('option:selected').val();
    var city_id = $('#cities').children('option:selected').val();
    var district_id = $('#districts').children('option:selected').val();
    var consignee = $('#consignee').val();
    var address = $('#address').val();
    var mobile = $('#mobile').val();
    var default_addr = $('#default_addr').is(':checked') ? 1 : 0;
    // alert('consignee='+consignee+' prov_id='+prov_id+'city_id='+city_id+' district_id='
    //         +district_id+' address='+address+' mobile='+mobile+' default_addr='+default_addr);
    if (consignee == '') {
        openDialog('', '收件人不能为空');
        return;
    }
    if (address == '') {
        openDialog('', '详细地址不能为空');
        return;
    }
    if (mobile == '') {
        openDialog('', '手机号不能为空');
        return;
    }
    var postdata = {
        'consignee': consignee,
        'province': prov_id,
        'city': city_id,
        'district': district_id,
        'address': address,
        'mobile': mobile,
        'default_addr': default_addr
    }
    $.post(appUrl + "/Usercenter/saveUserAddressSelection", postdata, function(res) {
        save_user_addressResponse(res);
    }, 'JSON');
}

function registerResponse(result) {
    if (result.code == 0) {
        signPageJump();
    } else {
        $("#register_main .login_prompt_1").text('该用户名已被注册')
    }
}

function save_user_addressResponse(res) {
    switch (res.code) {
        case 0:
            openDialog('', "保存用户地址成功");
            location.href = appUrl + "/Usercenter/userAddress";
            break;
        case 20011:
            openDialog('', "用户不存在");
            break;
        case 20002:
            openDialog('', "省、市、区不存在");
            break;
    }
}


function update_user_address() {
    // 获取省市区
    var prov_id = $('#provinces').children('option:selected').val();
    var city_id = $('#cities').children('option:selected').val();
    var district_id = $('#districts').children('option:selected').val();
    var consignee = $('#consignee').val();
    var address = $('#address').val();
    var mobile = $('#mobile').val();
    var default_addr = $('#default_addr').is(':checked') ? 1 : 0;
    // openDialog('','consignee='+consignee+' prov_id='+prov_id+'city_id='+city_id+' district_id='
    //         +district_id+' address='+address+' mobile='+mobile+' default_addr='+default_addr);
    if (consignee == '') {
        openDialog('', '收件人不能为空');
        return;
    }
    if (address == '') {
        openDialog('', '详细地址不能为空');
        return;
    }
    if (mobile == '') {
        openDialog('', '手机号不能为空');
        return;
    }
    var postdata = {
        'consignee': consignee,
        'province': prov_id,
        'city': city_id,
        'district': district_id,
        'address': address,
        'mobile': mobile,
        'default_addr': default_addr
    }
    $.post(appUrl + "/Usercenter/ajaxUpdateAddress", postdata, function(res) {
        update_user_addressResponse(res);
    }, 'JSON');
}


function update_user_addressResponse(res) {
    switch (res.code) {
        case 0:
            openDialog('', "修改用户地址成功");
            location.href = appUrl + "/Usercenter/userAddress";
            break;
        case 20011:
            openDialog('', "用户不存在");
            break;
        case 20002:
            openDialog('', "省、市、区不存在");
            break;
    }
}


//手机，邮箱格式验证
function isMobile_Email(value) {
    var m1 = new RegExp(/^13\d{9}$/g);
    var m2 = new RegExp(/^15[0-35-9]\d{8}$/g);
    var m3 = new RegExp(/^14[0-35-9]\d{8}$/g);
    var m4 = new RegExp(/^18[01-9]\d{8}$/g);

    var e1 = new RegExp(/^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/);

    if (m1.test(value) || (m2.test(value)) ||
        (m3.test(value)) || (m4.test(value))
    ) {
        return true;

    } else if (e1.test(value)) {
        return true;
    } else {
        return false;
    }
}

//登录或注册后页面跳转
function signPageJump() {
    var url = $("#signJumpPage").val();
    if (url == "") {
        location.reload();

    }

    window.location.href = url;
}

//用户登录反馈函数
function signInResponse(result) {

    if (result.code == 0) {
        signPageJump();
        return;
    }
    $("#login_main .login_prompt_1").text('用户名或密码错误');
}


//wwz Usercenter用户更新资料
function updateUserInfo() {

    var nickname = $("[name=nickname]").val();
    var birthday = $("#d11").val();
    /*  birthday = birthday.toString(birthday);
    var birthdayYear = $("#birthYear").find("option:selected").text();
    var birthdayMonth = $("#birthMonth").find("option:selected").text();
    var birthdayDay = $("#birthDay").find("option:selected").text();
    var birthdayYear = birthday.substring(0,4);
    var birthdayMonth = birthday.substring(6,7);
    var birthdayDay = birthday.substring(9,10);
*/

    // 处理错误年月日问题，2月不能有30号  4月不能有31号
    /*var birthdayOK = true;
    if (birthdayMonth != 1 && birthdayMonth != 3 && birthdayMonth != 5 && birthdayMonth != 7 && birthdayMonth != 8 && birthdayMonth != 10 && birthdayMonth != 12 && birthdayDay == 31) {
        birthdayOK = false;
    }
    if (!isLeapYear(birthdayYear) && birthdayMonth == 2 && birthdayDay > 28) {
        birthdayOK = false;
    }
    if (!birthdayOK) {
        openDialog('', '出生日期错误');
        return;
    }*/

    var postdata = {
        'nickname': nickname,
        'birthday': birthday
        /*'birthdayYear': birthdayYear,
        'birthdayMonth': birthdayMonth,
        'birthdayDay': birthdayDay*/
    }
    $.post(appUrl + "/Usercenter/updateUserInfo", postdata, function(res) {
        updateUserInfoResponse(res);
    }, 'JSON');
}

function isLeapYear(year) {
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) return true;
    else return false;
}

//wwz Usercenter更新资料反馈函数
function updateUserInfoResponse(res) {
    switch (res.code) {
        case 0:
            openDialog('', '更新成功');
            //location.reload();
            break;
        case 20011:
            openDialog('', '用户不存在');
            break;
        case 20012:
            openDialog('', '有非法字符');
            break;
        case 20018:
            openDialog('', '获取用户信息失败');
            break;
        case 20051:
            openDialog('', '日期错误');
            break;
        case 20013:
            openDialog('', '保存成功');
            break;
    }
}


//wwz Usercenter用户修改密码
function updatePassword() {

    var oldpassword = $("[name=oldpassword]").val();
    var password = $("[name=password]").val();
    var password2 = $("[name=password2]").val();

    if (oldpassword === "" || password === "" || password2 === "") {
        openDialog('', "密码不能为空");
        return;
    } else if (password != password2) {
        openDialog('', "两次密码输入不正确");
        return;
    } else {
        if (password.length > 16 || password.length < 7) {
            openDialog('', "密码过长或过短");
            return;
        };
        var postdata = {
            oldpassword: oldpassword,
            password: password
        }
        $.post(appUrl + "/Usercenter/updatePassword", postdata, function(res) {
            updatePasswordResponse(res);
        }, 'JSON');
    }
}

//wwz Usercenter用户修改密码反馈
function updatePasswordResponse(res) {
    switch (res.code) {
        case 0:
            openDialog('', "修改成功");
            break;
        case 20011:
            openDialog('', "用户不存在");
            break;
        case 20012:
            openDialog('', "有非法字符");
            break;
        case 20013:
            openDialog('', "修改失败");
            break;
        case 20020:
            openDialog('', "原密码错误");
            break;
    }
}

//Usercenter用户设置默认地址
function setDefaultAddress(addr_id) {
    postdata = {
        addr_id: addr_id
    }
    $.post(appUrl + "/Usercenter/setDefaultAddress", postdata, function(res) {
        setDefaultAddressResponse(res);
    }, 'JSON');
}

//Usercenter用户设置默认地址反馈
function setDefaultAddressResponse(res) {
    switch (res.code) {
        case 0:
            openDialog('', "修改成功");
            break;
        case 20003:
            openDialog('', "地址不存在");
            break;
        case 20008:
            openDialog('', "地址不属于该用户");
            break;
    }
}

//Usercenter用户删除地址
function deleteAddress() {
    var obj = document.getElementsByName('addr_id[]'); //选择所有name="'addr_id'"的对象，返回数组    
    var k = 0;
    //取到对象数组后，循环检测它是不是被选中 
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].checked) {
            k++;
        }
    }
    if (k == 0) {
        openDialog('', "未选中任何地址");
        return false;
    }
    document.getElementById('adlist').submit();
}

function cancelOrderDialog(orderId) {
    openDialog('', '您确认要取消此订单?', '关闭', null, '确定', function() {
        cancelOrder(orderId);
    });
}

function cancelOrder(orderId) {
    if (!orderId) return false;
    $.get(appUrl + '/Usercenter/cancelOrder/?oid=' + orderId, function(res) {
        cancelOrderResponse(res);
    }, 'JSON');
}

function cancelOrderResponse(res) {
    if (res.code == 0) {
        openDialog('', '取消订单成功', null, function() {
            location.reload();
        });
    } else {
        openDialog('', res.msg);
    }
}

//Usercenter用户激活优惠券
function activateBonus() {
    var bonus_code = $("[name=bonus_code]").val();
    var verify = $("[name=verify]").val();

    if (bonus_code === "") {
        openDialog('', "卡号不能为空");
    } else if (verify === "") {
        openDialog('', "验证码不能为空");
    } else {
        var postdata = {
            bonus_code: bonus_code,
            verify: verify
        }
        $.post(appUrl + "/Usercenter/activateBonus", postdata, function(res) {
            activateBonusResponse(res);
            updateVerify();
        }, 'JSON');
    }
}

//Usercenter用户激活优惠券反馈
function activateBonusResponse(res) {
    switch (res.code) {
        case -1:
            openDialog('', "验证码错误");
            break;
        case 0:
            openDialog('', "激活成功");
            location.reload();
            break;
        default:
            openDialog('', res.msg);
            break;
    }
}


//Usercenter用户激活礼品卡
function activateGiftcard() {
    var gc_key = $("[name=gc_key]").val();
    var verify = $("[name=verify]").val();

    if (gc_key === "") {
        openDialog('', "卡号不能为空");
        return false;
    } else if (verify === "") {
        openDialog('', "验证码不能为空");
        return false;
    } else {
        var postdata = {
            gc_key: gc_key,
            verify: verify
        }
        $.post(appUrl + "/Usercenter/activateGiftcard", postdata, function(res) {
            activateGiftcardResponse(res);
        }, 'JSON');
    }
}


//Usercenter用户激活礼品卡反馈
function activateGiftcardResponse(res) {
    switch (res.code) {
        case 0:
            openDialog('', "激活成功");
            location.reload();
            break;
        case -1:
            openDialog('', "验证码错误");
            break;
        case 70110:
            openDialog('', "礼品卡激活码不存在");
            break;
        case 70111:
            openDialog('', "礼品卡已过期");
            break;
        case 70112:
            openDialog('', "礼品卡未售出");
            break;
        case 70115:
            openDialog('', "礼品卡已激活");
            break;

    }
}

//刷新验证码
function updateVerify() {

    document.getElementById('verifyImg').src = appUrl + '/Users/verify/' + '?' + Math.random();
}

function cplink() {
    var str = $("#user-invite-link").val();
    if (window.clipboardData) {
        window.clipboardData.clearData();
        window.clipboardData.setData("Text", str);
        alert("复制成功！");
    } else {
        alert("浏览器不支持自动复制,请手动复制文本框的内容")
    }
}