empty_full_width = '[fullwidth background_color=\"\" background_image=\"\" background_parallax=\"none\" enable_mobile=\"no\" parallax_speed=\"0.3\" background_repeat=\"no-repeat\" background_position=\"left top\" video_url=\"\" video_aspect_ratio=\"16:9\" video_webm=\"\" video_mp4=\"\" video_ogv=\"\" video_preview_image=\"\" overlay_color=\"\" overlay_opacity=\"0.5\" video_mute=\"yes\" video_loop=\"yes\" fade=\"no\" border_size=\"0px\" border_color=\"\" border_style=\"\" padding_top=\"20\" padding_bottom=\"20\" padding_left=\"0\" padding_right=\"0\" hundred_percent=\"no\" equal_height_columns=\"no\" hide_on_mobile=\"no\" menu_anchor=\"\" class=\"\" id=\"\"][/fullwidth]'
opening_full_width = '[fullwidth background_color=\"\" background_image=\"http://growingtogethermetro.org/egc/wp-content/uploads/nashville-edited.jpg\" background_parallax=\"up\" enable_mobile=\"no\" parallax_speed=\"0.7\" background_repeat=\"no-repeat\" background_position=\"center top\" video_url=\"\" video_aspect_ratio=\"16:9\" video_webm=\"\" video_mp4=\"\" video_ogv=\"\" video_preview_image=\"\" overlay_color=\"\" overlay_opacity=\"0.5\" video_mute=\"yes\" video_loop=\"yes\" fade=\"no\" border_size=\"0px\" border_color=\"\" border_style=\"solid\" padding_top=\"20\" padding_bottom=\"20\" padding_left=\"0\" padding_right=\"0\" hundred_percent=\"no\" equal_height_columns=\"no\" hide_on_mobile=\"no\" menu_anchor=\"\" class=\"\" id=\"\"]'
opening_one_full = '[one_full last=\"yes\" spacing=\"yes\" center_content=\"no\" hide_on_mobile=\"no\" background_color=\"\" background_image=\"\" background_repeat=\"no-repeat\" background_position=\"left top\" border_position=\"all\" border_size=\"0px\" border_color=\"\" border_style=\"solid\" padding=\"\" margin_top=\"\" margin_bottom=\"\" animation_type=\"0\" animation_direction=\"down\" animation_speed=\"0.1\" class=\"region-text-box-header\" id=\"\"]'
opening_title = '[title size=\"1\" content_align=\"left\" style_type=\"default\" sep_color=\"\" margin_top=\"\" margin_bottom=\"\" class=\"region-title-header\" id=\"\"]'
closing_title = '[/title]'
closing_one_full = '[/one_full]'
one_fourth_ln = '[one_fourth last=\"no\" spacing=\"yes\" center_content=\"no\" hide_on_mobile=\"no\" background_color=\"\" background_image=\"\" background_repeat=\"no-repeat\" background_position=\"left top\" border_position=\"all\" border_size=\"0px\" border_color=\"\" border_style=\"solid\" padding=\"\" margin_top=\"\" margin_bottom=\"\" animation_type=\"fade\" animation_direction=\"down\" animation_speed=\"0.5\" class=\"region-text-box\" id=\"\"]'
one_fourth_ly = '[one_fourth last=\"yes\" spacing=\"yes\" center_content=\"no\" hide_on_mobile=\"no\" background_color=\"\" background_image=\"\" background_repeat=\"no-repeat\" background_position=\"left top\" border_position=\"all\" border_size=\"0px\" border_color=\"\" border_style=\"solid\" padding=\"\" margin_top=\"\" margin_bottom=\"\" animation_type=\"fade\" animation_direction=\"down\" animation_speed=\"0.5\" class=\"region-text-box\" id=\"\"]'
opener = '[fusion_text]'
closer = '[/fusion_text][/one_fourth]'
closing_full_width = '[/fullwidth]'

title = ''
description = ''
links = [

]



def make_quarters(links,title,description):
	print empty_full_width + opening_full_width + opening_one_full + opening_title + title + closing_title + description + closing_one_full
	for i in range(1,len(links)+1):
		if i % 4 == 0:
			print  one_fourth_ly + opener + links[i-1] + closer
		elif i == len(links):
			print one_fourth_ly + opener + links[i-1] + closer
		else:
			print one_fourth_ln + opener + links[i-1] + closer 
	print closing_full_width
		

make_quarters(links,title,description)

