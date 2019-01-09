package org.chm.course.controller;

import com.alibaba.dubbo.config.annotation.Reference;
import org.chm.course.dto.CourseDTO;
import org.chm.course.service.ICourseService;
import org.chm.thrift.user.dto.UserDTO;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

@Controller
@RequestMapping("/course")
public class CourseController {

    @Reference
    private ICourseService courseService;

    @RequestMapping(value = "/courseList", method = RequestMethod.GET)
    @ResponseBody
    public List<CourseDTO> courseList(HttpServletRequest request) {
        UserDTO user = (UserDTO) request.getAttribute("user");
        System.out.println(user);
        return courseService.courseList();
    }

}
