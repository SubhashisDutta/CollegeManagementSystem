-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2021 at 07:23 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sd`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendanceinfo`
--

CREATE TABLE `attendanceinfo` (
  `name` varchar(100) NOT NULL,
  `rol` varchar(100) NOT NULL,
  `unirol` varchar(100) NOT NULL,
  `cs` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `sub` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `attendance` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendanceinfo`
--

INSERT INTO `attendanceinfo` (`name`, `rol`, `unirol`, `cs`, `course`, `department`, `sub`, `date`, `attendance`) VALUES
('Suman', '14', '1090308022', '6th', 'b.tech', 'ECE', 'CN', '01/06/21', 'present'),
('Suprotim', '13', '1090308021', '6th', 'b.tech', 'ECE', 'CN', '01/06/21', 'present'),
('Sudhya', '15', '1090308023', '6th', 'b.tech', 'ECE', 'CN', '05/06/21', 'present'),
('Subhashis', '16', '1090308024', '6th', 'b.tech', 'ECE', 'CN', '01/06/21', 'present'),
('Sudhya', '15', '1090308023', '6th', 'b.tech', 'ECE', 'CN', '05/06/21', 'present'),
('Suprotim', '13', '1090308021', '6th', 'b.tech', 'ECE', 'CN', '05/06/21', 'present'),
('Suman', '14', '1090308022', '6th', 'b.tech', 'ECE', 'CN', '06/06/21', 'present'),
('Subhashis', '16', '1090308024', '6th', 'b.tech', 'ECE', 'CN', '01/06/21', 'present');

-- --------------------------------------------------------

--
-- Table structure for table `ca`
--

CREATE TABLE `ca` (
  `name` varchar(100) NOT NULL,
  `rol` varchar(100) NOT NULL,
  `unirol` varchar(100) NOT NULL,
  `cs` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `sub` varchar(100) NOT NULL,
  `marks` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ca`
--

INSERT INTO `ca` (`name`, `rol`, `unirol`, `cs`, `course`, `department`, `sub`, `marks`) VALUES
('SUMAN PURKAIT', '14', '1090308022', '6th', 'B.Tech', 'ECE', 'Computer Network', '24/25'),
('SUPROTIM DATTA', '13', '1090308021', '6th', 'B.Tech', 'ECE', 'Computer Network', '24/25'),
('SUBHASHIS DUTTA', '16', '1090308024', '6th', 'B.Tech', 'ECE', 'Computer Network', '14/25'),
('SUDHYABRATA GUHA', '15', '1090308023', '6th', 'B.Tech', 'ECE', 'Analog CKT', '24/25');

-- --------------------------------------------------------

--
-- Table structure for table `caminfo`
--

CREATE TABLE `caminfo` (
  `name` varchar(100) NOT NULL,
  `rol` varchar(100) NOT NULL,
  `unirol` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mob` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `cs` varchar(100) NOT NULL,
  `sgp` varchar(100) NOT NULL,
  `placement` varchar(100) NOT NULL,
  `cn` varchar(100) NOT NULL,
  `sld` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `caminfo`
--

INSERT INTO `caminfo` (`name`, `rol`, `unirol`, `email`, `mob`, `address`, `course`, `department`, `cs`, `sgp`, `placement`, `cn`, `sld`) VALUES
('Suman Purkait', '14', '1090308022', 'suman@gmail.com', '9647632741', 'Diamond Harbour', 'B.tech', 'ECE', '6th', '7.77', 'selected', 'TCS', '01/06/21'),
('Suprotim Datta', '13', '1090308021', 'suprotim@gmail.com', '4536782741', 'Kolkata', 'B.tech', 'ECE', '6th', '8.00', 'selected', 'CTS', '02/06/21'),
('Subhashis Dutta', '16', '1090308024', 'subha@gmail.com', '3456782741', 'salt-lake', 'B.tech', 'ECE', '6th', '8.02', 'selected', 'Google', '05/06/21'),
('Sudhyabrata Guha', '15', '1090308023', 'sudhya@gmail.com', '7676982741', 'Kolkata', 'B.tech', 'ECE', '6th', '7.77', 'selected', 'amazon', '02/06/21');

-- --------------------------------------------------------

--
-- Table structure for table `college`
--

CREATE TABLE `college` (
  `fnm` varchar(40) NOT NULL,
  `lnm` varchar(40) NOT NULL,
  `contact` varchar(40) NOT NULL,
  `dob` varchar(40) NOT NULL,
  `course` varchar(40) NOT NULL,
  `gen` varchar(40) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `cpass` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `college`
--

INSERT INTO `college` (`fnm`, `lnm`, `contact`, `dob`, `course`, `gen`, `email`, `password`, `cpass`) VALUES
('Subhashis', 'Dattu', '7047496718', '4/1/99', 'BTECH', '', 'subhashis@gmail.com', '1234', '1234'),
('sudhya', 'Guha', '5648671967', '5/18/21', 'BTECH', 'Male', 'sudhya@gmail.com', '1234', '1234'),
('Suman ', 'Purkait', '7047496718', '11/25/99', 'BTECH', 'Male', 'suman@gmail.com', '1234', '1234'),
('Suprotim', 'Datta', '7856465634', '5/5/99', 'BTECH', '', 'suprotim@nsec.in', '1234', '1234'),
('Chira', 'Dutta', '7089234578', '25/06/62', 'BTECH', 'Male', 'chira@nsec.ac.in', '1234', '1234'),
('Sneha ', 'Halder', '9867342564', '6/1/21', 'BCA', 'Female', 'sneha@gmail.com', '1234', '1234'),
('admin', 'college', '8967234516', '6/1/21', 'BTECH', 'Male', 'nsec@ac.in', '1234', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `name` varchar(40) NOT NULL,
  `rol` varchar(40) NOT NULL,
  `cs` varchar(40) NOT NULL,
  `sgp` varchar(40) NOT NULL,
  `course` varchar(40) NOT NULL,
  `department` varchar(40) NOT NULL,
  `fd` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`name`, `rol`, `cs`, `sgp`, `course`, `department`, `fd`) VALUES
('Suman Purkait', '14', '6th', '8.21', 'B.Tech', 'ECE', '00.00'),
('Suprotim Datta', '13', '6th', '8.40', 'B.Tech', 'ECE', '00.00'),
('Subhashis Dutta', '16', '6th', '8.22', 'B.Tech', 'ECE', '45000'),
('Ankita Parui', '21', '6th', '8.66', 'B.Tech', 'ECE', '36000');

-- --------------------------------------------------------

--
-- Table structure for table `labmarksinfo`
--

CREATE TABLE `labmarksinfo` (
  `name` varchar(100) NOT NULL,
  `rol` varchar(100) NOT NULL,
  `unirol` varchar(100) NOT NULL,
  `cs` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `sub` varchar(100) NOT NULL,
  `labmarks` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `labmarksinfo`
--

INSERT INTO `labmarksinfo` (`name`, `rol`, `unirol`, `cs`, `course`, `department`, `sub`, `labmarks`) VALUES
('Suman Purkait', '14', '1090308022', '6th', 'B.Tech', 'ECE', 'Control system Lab', '38/40'),
('Suprotim Datta', '13', '1090308021', '6th', 'B.Tech', 'ECE', 'Control system Lab', '40/40'),
('Sudhyabrata Guha', '15', '1090308023', '6th', 'B.Tech', 'ECE', 'Control system Lab', '40/40'),
('Subhashis Dutta', '16', '1090308024', '6th', 'B.Tech', 'ECE', 'Control system Lab', '40/40');

-- --------------------------------------------------------

--
-- Table structure for table `library`
--

CREATE TABLE `library` (
  `memtype` varchar(100) NOT NULL,
  `reference` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mob` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `dep` varchar(100) NOT NULL,
  `bookid` varchar(100) NOT NULL,
  `booktitle` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `dd` varchar(100) NOT NULL,
  `dl` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `library`
--

INSERT INTO `library` (`memtype`, `reference`, `Name`, `Address`, `email`, `mob`, `course`, `dep`, `bookid`, `booktitle`, `author`, `dob`, `dd`, `dl`) VALUES
('Student', '820191', 'Suchismita DasMahapatra', 'Kolkata', 'suchismita@gmail.com', '7047496718', 'B.Tech', 'ECE', '9672B', 'Basic Electrical Engineering', '23/04/21', 'Suchismita DasMahapatra', 'ECE', '9672B'),
('Student', '820191', 'Sudhyabrata Guha', 'Kolkata', 'sudhy@gmail.com', '6788970989', 'B.Tech', 'ECE', '8587B', 'control system', 'M.Saha', '05/06/21', '04/06/21', '00.00'),
('Student', '820191', 'Suprotim Datta', 'Kolkata', 'supro@gmail.com', '6756789789', 'B.Tech', 'ECE', '4678B', 'EM Theory', 'S.M Paul', '07/05/21', '06/06/21', '00.00');

-- --------------------------------------------------------

--
-- Table structure for table `regadmi`
--

CREATE TABLE `regadmi` (
  `fnm` varchar(40) NOT NULL,
  `lnm` varchar(40) NOT NULL,
  `contact` varchar(40) NOT NULL,
  `dob` varchar(40) NOT NULL,
  `course` varchar(40) NOT NULL,
  `gen` varchar(40) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(40) NOT NULL,
  `cpass` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `regadmi`
--

INSERT INTO `regadmi` (`fnm`, `lnm`, `contact`, `dob`, `course`, `gen`, `email`, `password`, `cpass`) VALUES
('Dhiru', 'Mondal', '7834562734', '6/13/62', 'SELECT', 'Male', 'nsec@ac.in', '1234', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `regtea`
--

CREATE TABLE `regtea` (
  `fnm` varchar(40) NOT NULL,
  `lnm` varchar(40) NOT NULL,
  `contact` varchar(40) NOT NULL,
  `dob` varchar(40) NOT NULL,
  `course` varchar(40) NOT NULL,
  `gen` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `cpass` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `regtea`
--

INSERT INTO `regtea` (`fnm`, `lnm`, `contact`, `dob`, `course`, `gen`, `email`, `password`, `cpass`) VALUES
('Kousik', 'Dutta', '5678943438', '6/25/70', 'BTECH', 'Male', 'kousik@gmail.com', '1234', '1234'),
('Chira', 'Dutta', '745768787', '6/5/21', 'BTECH', 'Male', 'chira@gmail.com', '1234', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `teacherinfo`
--

CREATE TABLE `teacherinfo` (
  `name` varchar(100) NOT NULL,
  `deptno` varchar(100) NOT NULL,
  `hiredate` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mob` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `sub` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacherinfo`
--

INSERT INTO `teacherinfo` (`name`, `deptno`, `hiredate`, `department`, `email`, `mob`, `course`, `sub`, `qualification`) VALUES
('Ankita Saha', '1030837', '25/12/2011', 'ECE', 'ankita@gmail.com', '8967342658', 'B.Tech', 'Digital Electronics', 'M.Tech'),
('Kousik Dutta', '109786', '22/12/2000', 'ECE', 'kousik@gmail.com', '657342658', 'B.Tech', 'EM Theory', 'Msc,PhD');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
