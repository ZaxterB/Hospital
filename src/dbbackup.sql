--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3 (Ubuntu 12.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 12.3 (Ubuntu 12.3-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: hospital; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE hospital WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_GB.UTF-8' LC_CTYPE = 'en_GB.UTF-8';


ALTER DATABASE hospital OWNER TO postgres;

\connect hospital

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bedevent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bedevent (
    bedeventid serial NOT NULL,
    eventtime timestamp without time zone NOT NULL,
    eventtype smallint NOT NULL,
    patientid integer NOT NULL,
    bedid smallint NOT NULL,
    monitortypeid integer NOT NULL
);


ALTER TABLE public.bedevent OWNER TO postgres;

--
-- Name: staffevent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.staffevent (
    staffeventid serial NOT NULL,
    eventtime timestamp without time zone NOT NULL,
    type smallint NOT NULL,
    staffid integer NOT NULL
);


ALTER TABLE public.staffevent OWNER TO postgres;

--
-- Name: AllEvents; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public."AllEvents" AS
 SELECT bedevent.eventtime,
    bedevent.type,
    bedevent.bedeventid,
    bedevent.patientid,
    bedevent.bedid AS bed,
    bedevent.monitortypeid AS monitortype,
    staffevent.staffeventid,
    staffevent.staffid
   FROM (public.bedevent bedevent(bedeventid, eventtime, type, patientid, bedid, monitortypeid)
     JOIN public.staffevent USING (eventtime, type));


ALTER TABLE public."AllEvents" OWNER TO postgres;

--
-- Name: bed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bed (
    bedid serial NOT NULL,
    bednumber integer NOT NULL
);


ALTER TABLE public.bed OWNER TO postgres;

--
-- Name: bedmodule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bedmodule (
    bedmoduleid serial NOT NULL,
    bedid integer NOT NULL,
    moduleid integer NOT NULL
);


ALTER TABLE public.bedmodule OWNER TO postgres;

--
-- Name: module; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.module (
    moduleid serial NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.module OWNER TO postgres;

--
-- Name: modulemonitor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.modulemonitor (
    modulemonitorid serial NOT NULL,
    monitortypeid integer NOT NULL,
    moduleid integer NOT NULL,
    minval numeric NOT NULL,
    maxval numeric NOT NULL
);


ALTER TABLE public.modulemonitor OWNER TO postgres;

--
-- Name: monitortype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monitortype (
    monitortypeid serial NOT NULL,
    name character varying NOT NULL,
    unit character varying NOT NULL,
    defaultmax numeric(5,2) NOT NULL,
    defaultmin numeric(5,2) NOT NULL,
    dangermax numeric(5,2) NOT NULL,
    dangermin numeric(5,2) NOT NULL
);


ALTER TABLE public.monitortype OWNER TO postgres;

--
-- Name: patient; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.patient (
    patientid serial NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.patient OWNER TO postgres;

--
-- Name: shift; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shift (
    shiftid serial NOT NULL,
    staffid integer NOT NULL,
    start timestamp without time zone NOT NULL,
    currentend timestamp without time zone NOT NULL
);


ALTER TABLE public.shift OWNER TO postgres;

--
-- Name: staff; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.staff (
    staffid serial NOT NULL,
    name character varying NOT NULL,
    email character varying,
    telnumber character varying,
    stafftype smallint NOT NULL
);


ALTER TABLE public.staff OWNER TO postgres;

--
-- Name: COLUMN staff.stafftype; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.staff.stafftype IS '1=nurse, 2=consultant';


--
-- Data for Name: bed; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bed (bedid, bednumber) FROM stdin;
1	1
2	2
3	3
4	4
\.


--
-- Data for Name: bedevent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bedevent (bedeventid, eventtime, eventtype, patientid, bedid, monitortypeid) FROM stdin;
\.


--
-- Data for Name: bedmodule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bedmodule (bedmoduleid, bedid, moduleid) FROM stdin;
1	1	1
2	1	2
4	2	3
5	3	1
6	3	2
7	3	3
8	3	4
\.


--
-- Data for Name: module; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.module (moduleid, name) FROM stdin;
1	Pulse
2	Breathing
3	Blood pressure
4	Temperature
5	Breathing
\.


--
-- Data for Name: modulemonitor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.modulemonitor (modulemonitorid, monitortypeid, moduleid, minval, maxval) FROM stdin;
1	1	1	66	78
2	2	2	36	38
3	3	3	80	120
4	4	3	60	80
5	5	4	35.5	37.5
6	2	5	37	39
\.


--
-- Data for Name: monitortype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.monitortype (monitortypeid, name, unit, defaultmax, defaultmin, dangermax, dangermin) FROM stdin;
1	Pulse rate	Bps	78.00	66.00	100.00	54.00
2	Breathing rate	Bpm	38.00	36.00	40.00	35.00
3	Systolic pressure	mmHg	120.00	80.00	180.00	60.00
4	Diastolic pressure	mmHg	80.00	60.00	110.00	50.00
5	Temperature	degC	37.50	35.50	38.00	35.00
\.


--
-- Data for Name: patient; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.patient (patientid, name) FROM stdin;
1   Alice
2   Bob
\.


--
-- Data for Name: shift; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shift (shiftid, staffid, start, currentend) FROM stdin;
1	1	2020-05-16 16:00:00	2020-05-17 00:00:00
2	2	2020-05-16 16:00:00	2020-05-17 00:00:00
3	3	2020-05-16 16:00:00	2020-05-17 00:00:00
4	4	2020-05-16 16:00:00	2020-05-17 00:00:00
\.


--
-- Data for Name: staff; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.staff (staffid, name, email, telnumber, stafftype) FROM stdin;
1	Edward Brown	ed.brown@nhs.net	+44 4040 234984	1
2	Evelyn Entwhistle	evelyn.entwhistle@nhs.net	+44 9823 943731	2
3	Bob Ball	bob.ball@nhs.net	+44 3765 736250	1
4	Steve Black	steve.black@nhs.net	+44 6565 968130	1
\.


--
-- Data for Name: staffevent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.staffevent (staffeventid, eventtime, type, staffid) FROM stdin;
\.


--
-- Name: bedevent BedEvent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT "BedEvent_pkey" PRIMARY KEY (bedeventid);


--
-- Name: bed Bed_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bed
    ADD CONSTRAINT "Bed_pkey" PRIMARY KEY (bedid);


--
-- Name: monitortype Monitortype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitortype
    ADD CONSTRAINT "Monitortype_pkey" PRIMARY KEY (monitortypeid);


--
-- Name: patient Patient_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient
    ADD CONSTRAINT "Patient_pkey" PRIMARY KEY (patientid);


--
-- Name: staffevent StaffEvent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staffevent
    ADD CONSTRAINT "StaffEvent_pkey" PRIMARY KEY (staffeventid);


--
-- Name: staff Staff_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT "Staff_pkey" PRIMARY KEY (staffid);


--
-- Name: bedmodule bedmodule_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedmodule
    ADD CONSTRAINT bedmodule_pkey PRIMARY KEY (bedmoduleid);


--
-- Name: module module_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.module
    ADD CONSTRAINT module_pkey PRIMARY KEY (moduleid);


--
-- Name: modulemonitor modulemonitor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modulemonitor
    ADD CONSTRAINT modulemonitor_pkey PRIMARY KEY (modulemonitorid);


--
-- Name: shift shift_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift
    ADD CONSTRAINT shift_pkey PRIMARY KEY (shiftid);


--
-- Name: bedevent bedevent_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT bedevent_fk FOREIGN KEY (bedid) REFERENCES public.bed(bedid);


--
-- Name: bedmodule bedid_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedmodule
    ADD CONSTRAINT bedid_fk FOREIGN KEY (bedid) REFERENCES public.bed(bedid) NOT VALID;


--
-- Name: bedmodule moduleid_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedmodule
    ADD CONSTRAINT moduleid_fk FOREIGN KEY (moduleid) REFERENCES public.module(moduleid) NOT VALID;


--
-- Name: modulemonitor moduleid_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modulemonitor
    ADD CONSTRAINT moduleid_fk FOREIGN KEY (moduleid) REFERENCES public.module(moduleid) NOT VALID;


--
-- Name: bedevent monitortype_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT monitortype_fk FOREIGN KEY (monitortypeid) REFERENCES public.monitortype(monitortypeid);


--
-- Name: modulemonitor monitortype_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modulemonitor
    ADD CONSTRAINT monitortype_fk FOREIGN KEY (modulemonitorid) REFERENCES public.monitortype(monitortypeid) NOT VALID;


--
-- Name: bedevent patient_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT patient_fk FOREIGN KEY (patientid) REFERENCES public.patient(patientid);


--
-- Name: shift staff_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift
    ADD CONSTRAINT staff_fk FOREIGN KEY (staffid) REFERENCES public.staff(staffid);


--
-- Name: staffevent staffevent_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staffevent
    ADD CONSTRAINT staffevent_fk FOREIGN KEY (staffid) REFERENCES public.staff(staffid);


--
-- PostgreSQL database dump complete
--

