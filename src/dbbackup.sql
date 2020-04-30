--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Ubuntu 12.2-2.pgdg19.10+1)
-- Dumped by pg_dump version 12.2 (Ubuntu 12.2-2.pgdg19.10+1)

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
-- Name: hospital; Type: DATABASE; Schema: -; Owner: timc
--

CREATE DATABASE hospital WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_GB.UTF-8' LC_CTYPE = 'en_GB.UTF-8';


ALTER DATABASE hospital OWNER TO timc;

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
-- Name: bedevent; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.bedevent (
    bedeventid integer NOT NULL,
    eventtime timestamp without time zone NOT NULL,
    eventtype smallint NOT NULL,
    patientid integer NOT NULL,
    bedid smallint NOT NULL,
    monitortypeid integer NOT NULL
);


ALTER TABLE public.bedevent OWNER TO timc;

--
-- Name: staffevent; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.staffevent (
    staffeventid integer NOT NULL,
    eventtime timestamp without time zone NOT NULL,
    type smallint NOT NULL,
    staffid integer NOT NULL
);


ALTER TABLE public.staffevent OWNER TO timc;

--
-- Name: AllEvents; Type: VIEW; Schema: public; Owner: timc
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


ALTER TABLE public."AllEvents" OWNER TO timc;

--
-- Name: bed; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.bed (
    bedid integer NOT NULL,
    bednumber integer NOT NULL
);


ALTER TABLE public.bed OWNER TO timc;

--
-- Name: bedmodule; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.bedmodule (
    bedmoduleid integer NOT NULL,
    bedid integer NOT NULL,
    moduleid integer NOT NULL
);


ALTER TABLE public.bedmodule OWNER TO timc;

--
-- Name: module; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.module (
    moduleid integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.module OWNER TO timc;

--
-- Name: monitortype; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.monitortype (
    monitortypeid integer NOT NULL,
    moduleid integer NOT NULL,
    name character varying NOT NULL,
    unit character varying NOT NULL,
    defaultmax numeric(5,2) NOT NULL,
    defaultmin numeric(5,2) NOT NULL,
    dangermax numeric(5,2) NOT NULL,
    dangermin numeric(5,2) NOT NULL
);


ALTER TABLE public.monitortype OWNER TO timc;

--
-- Name: patient; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.patient (
    patientid integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.patient OWNER TO timc;

--
-- Name: staff; Type: TABLE; Schema: public; Owner: timc
--

CREATE TABLE public.staff (
    staffid integer NOT NULL,
    name character varying NOT NULL,
    email character varying,
    number character varying,
    type smallint NOT NULL
);


ALTER TABLE public.staff OWNER TO timc;

--
-- Data for Name: bed; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.bed (bedid, bednumber) FROM stdin;
1	1
2	2
3	3
4	4
\.


--
-- Data for Name: bedevent; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.bedevent (bedeventid, eventtime, eventtype, patientid, bedid, monitortypeid) FROM stdin;
\.


--
-- Data for Name: bedmodule; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.bedmodule (bedmoduleid, bedid, moduleid) FROM stdin;
\.


--
-- Data for Name: module; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.module (moduleid, name) FROM stdin;
1	Pulse
2	Breathing
3	Blood pressure
4	Temperature
\.


--
-- Data for Name: monitortype; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.monitortype (monitortypeid, moduleid, name, unit, defaultmax, defaultmin, dangermax, dangermin) FROM stdin;
1	1	Pulse rate	Bps	78.00	66.00	100.00	54.00
2	2	Breathing rate	Bpm	38.00	36.00	40.00	35.00
3	3	Systolic pressure	mmHg	120.00	80.00	180.00	60.00
4	3	Diastolic pressure	mmHg	80.00	60.00	110.00	50.00
5	4	Temperature	degC	37.50	35.50	38.00	35.00
\.


--
-- Data for Name: patient; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.patient (patientid, name) FROM stdin;
\.


--
-- Data for Name: staff; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.staff (staffid, name, email, number, type) FROM stdin;
1	Edward Brown	ed.brown@nhs.net	+44 4040 234984	1
2	Evelyn Entwhistle	evelyn.entwhistle@nhs.net	+44 9823 943731	2
3	Bob Ball	bob.ball@nhs.net	+44 3765 736250	1
4	Steve Black	steve.black@nhs.net	+44 6565 968130	1
\.


--
-- Data for Name: staffevent; Type: TABLE DATA; Schema: public; Owner: timc
--

COPY public.staffevent (staffeventid, eventtime, type, staffid) FROM stdin;
\.


--
-- Name: bedevent BedEvent_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT "BedEvent_pkey" PRIMARY KEY (bedeventid);


--
-- Name: bed Bed_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.bed
    ADD CONSTRAINT "Bed_pkey" PRIMARY KEY (bedid);


--
-- Name: monitortype Monitortype_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.monitortype
    ADD CONSTRAINT "Monitortype_pkey" PRIMARY KEY (monitortypeid);


--
-- Name: patient Patient_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.patient
    ADD CONSTRAINT "Patient_pkey" PRIMARY KEY (patientid);


--
-- Name: staffevent StaffEvent_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.staffevent
    ADD CONSTRAINT "StaffEvent_pkey" PRIMARY KEY (staffeventid);


--
-- Name: staff Staff_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.staff
    ADD CONSTRAINT "Staff_pkey" PRIMARY KEY (staffid);


--
-- Name: bedmodule bedmodule_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.bedmodule
    ADD CONSTRAINT bedmodule_pkey PRIMARY KEY (bedmoduleid);


--
-- Name: module module_pkey; Type: CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.module
    ADD CONSTRAINT module_pkey PRIMARY KEY (moduleid);


--
-- Name: bedevent bedevent_fk; Type: FK CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT bedevent_fk FOREIGN KEY (bedid) REFERENCES public.bed(bedid);


--
-- Name: monitortype module_fk; Type: FK CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.monitortype
    ADD CONSTRAINT module_fk FOREIGN KEY (monitortypeid) REFERENCES public.module(moduleid) NOT VALID;


--
-- Name: bedevent monitortype_fk; Type: FK CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT monitortype_fk FOREIGN KEY (monitortypeid) REFERENCES public.monitortype(monitortypeid);


--
-- Name: bedevent patient_fk; Type: FK CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.bedevent
    ADD CONSTRAINT patient_fk FOREIGN KEY (patientid) REFERENCES public.patient(patientid);


--
-- Name: staffevent staffevent_fk; Type: FK CONSTRAINT; Schema: public; Owner: timc
--

ALTER TABLE ONLY public.staffevent
    ADD CONSTRAINT staffevent_fk FOREIGN KEY (staffid) REFERENCES public.staff(staffid);


--
-- PostgreSQL database dump complete
--

