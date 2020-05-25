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
-- Name: bed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bed (
    bedid integer NOT NULL,
    bednumber integer NOT NULL
);


ALTER TABLE public.bed OWNER TO postgres;

--
-- Name: bedevent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bedevent (
    bedeventid integer NOT NULL,
    eventtime timestamp without time zone NOT NULL,
    eventtype smallint NOT NULL,
    patientid integer,
    bedid smallint NOT NULL,
    monitortypeid integer
);


ALTER TABLE public.bedevent OWNER TO postgres;

--
-- Name: event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event (
    eventid integer NOT NULL,
    description character varying NOT NULL
);


ALTER TABLE public.event OWNER TO postgres;

--
-- Name: TABLE event; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.event IS 'decode events to readable text';


--
-- Name: monitortype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monitortype (
    monitortypeid integer NOT NULL,
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
    patientid integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.patient OWNER TO postgres;

--
-- Name: staff; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.staff (
    staffid integer NOT NULL,
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
-- Name: staffevent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.staffevent (
    staffeventid integer NOT NULL,
    eventtime timestamp without time zone NOT NULL,
    eventtype smallint NOT NULL,
    staffid integer NOT NULL
);


ALTER TABLE public.staffevent OWNER TO postgres;

--
-- Name: AllEvents; Type: VIEW; Schema: public; Owner: timc
--

CREATE VIEW public."AllEvents" AS
 SELECT be.eventtime,
    ev.description AS eventtype,
    ((((('Bed '::text || bd.bednumber) || ' '::text) || (COALESCE(pa.name, ''::character varying))::text) || ' '::text) || (COALESCE(mt.name, ''::character varying))::text) AS description
   FROM ((public.bedevent be
     LEFT JOIN public.patient pa ON ((be.patientid = pa.patientid)))
     LEFT JOIN public.monitortype mt ON ((be.monitortypeid = mt.monitortypeid))),
    public.event ev,
    public.bed bd
  WHERE ((be.eventtype = ev.eventid) AND (be.bedid = bd.bedid))
UNION
 SELECT se.eventtime,
    ev.description AS eventtype,
    st.name AS description
   FROM public.staffevent se,
    public.event ev,
    public.staff st
  WHERE ((se.eventtype = ev.eventid) AND (se.staffid = st.staffid))
  ORDER BY 1;


ALTER TABLE public."AllEvents" OWNER TO timc;

--
-- Name: bed_bedid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bed_bedid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bed_bedid_seq OWNER TO postgres;

--
-- Name: bed_bedid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bed_bedid_seq OWNED BY public.bed.bedid;


--
-- Name: bedevent_bedeventid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bedevent_bedeventid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bedevent_bedeventid_seq OWNER TO postgres;

--
-- Name: bedevent_bedeventid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bedevent_bedeventid_seq OWNED BY public.bedevent.bedeventid;


--
-- Name: bedmodule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bedmodule (
    bedmoduleid integer NOT NULL,
    bedid integer NOT NULL,
    moduleid integer NOT NULL
);


ALTER TABLE public.bedmodule OWNER TO postgres;

--
-- Name: bedmodule_bedmoduleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bedmodule_bedmoduleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bedmodule_bedmoduleid_seq OWNER TO postgres;

--
-- Name: bedmodule_bedmoduleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bedmodule_bedmoduleid_seq OWNED BY public.bedmodule.bedmoduleid;


--
-- Name: module; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.module (
    moduleid integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.module OWNER TO postgres;

--
-- Name: module_moduleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.module_moduleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.module_moduleid_seq OWNER TO postgres;

--
-- Name: module_moduleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.module_moduleid_seq OWNED BY public.module.moduleid;


--
-- Name: modulemonitor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.modulemonitor (
    modulemonitorid integer NOT NULL,
    monitortypeid integer NOT NULL,
    moduleid integer NOT NULL,
    minval numeric NOT NULL,
    maxval numeric NOT NULL
);


ALTER TABLE public.modulemonitor OWNER TO postgres;

--
-- Name: modulemonitor_modulemonitorid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.modulemonitor_modulemonitorid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.modulemonitor_modulemonitorid_seq OWNER TO postgres;

--
-- Name: modulemonitor_modulemonitorid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.modulemonitor_modulemonitorid_seq OWNED BY public.modulemonitor.modulemonitorid;


--
-- Name: monitortype_monitortypeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monitortype_monitortypeid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.monitortype_monitortypeid_seq OWNER TO postgres;

--
-- Name: monitortype_monitortypeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monitortype_monitortypeid_seq OWNED BY public.monitortype.monitortypeid;


--
-- Name: patient_patientid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.patient_patientid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patient_patientid_seq OWNER TO postgres;

--
-- Name: patient_patientid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.patient_patientid_seq OWNED BY public.patient.patientid;


--
-- Name: shift; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shift (
    shiftid integer NOT NULL,
    staffid integer NOT NULL,
    start timestamp without time zone NOT NULL,
    currentend timestamp without time zone NOT NULL
);


ALTER TABLE public.shift OWNER TO postgres;

--
-- Name: shift_shiftid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shift_shiftid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shift_shiftid_seq OWNER TO postgres;

--
-- Name: shift_shiftid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shift_shiftid_seq OWNED BY public.shift.shiftid;


--
-- Name: staff_staffid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.staff_staffid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staff_staffid_seq OWNER TO postgres;

--
-- Name: staff_staffid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.staff_staffid_seq OWNED BY public.staff.staffid;


--
-- Name: staffevent_staffeventid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.staffevent_staffeventid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.staffevent_staffeventid_seq OWNER TO postgres;

--
-- Name: staffevent_staffeventid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.staffevent_staffeventid_seq OWNED BY public.staffevent.staffeventid;


--
-- Name: bed bedid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bed ALTER COLUMN bedid SET DEFAULT nextval('public.bed_bedid_seq'::regclass);


--
-- Name: bedevent bedeventid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedevent ALTER COLUMN bedeventid SET DEFAULT nextval('public.bedevent_bedeventid_seq'::regclass);


--
-- Name: bedmodule bedmoduleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bedmodule ALTER COLUMN bedmoduleid SET DEFAULT nextval('public.bedmodule_bedmoduleid_seq'::regclass);


--
-- Name: module moduleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.module ALTER COLUMN moduleid SET DEFAULT nextval('public.module_moduleid_seq'::regclass);


--
-- Name: modulemonitor modulemonitorid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modulemonitor ALTER COLUMN modulemonitorid SET DEFAULT nextval('public.modulemonitor_modulemonitorid_seq'::regclass);


--
-- Name: monitortype monitortypeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monitortype ALTER COLUMN monitortypeid SET DEFAULT nextval('public.monitortype_monitortypeid_seq'::regclass);


--
-- Name: patient patientid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.patient ALTER COLUMN patientid SET DEFAULT nextval('public.patient_patientid_seq'::regclass);


--
-- Name: shift shiftid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shift ALTER COLUMN shiftid SET DEFAULT nextval('public.shift_shiftid_seq'::regclass);


--
-- Name: staff staffid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staff ALTER COLUMN staffid SET DEFAULT nextval('public.staff_staffid_seq'::regclass);


--
-- Name: staffevent staffeventid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.staffevent ALTER COLUMN staffeventid SET DEFAULT nextval('public.staffevent_staffeventid_seq'::regclass);


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
8	2020-05-23 14:16:39.68028	5	2	1	1
9	2020-05-23 14:16:40.791093	8	2	1	1
10	2020-05-24 17:01:09.529099	5	2	1	2
11	2020-05-24 17:01:11.60526	5	2	1	2
12	2020-05-24 17:01:12.605671	5	2	1	2
13	2020-05-24 17:01:13.605843	5	2	1	2
14	2020-05-24 17:01:14.606249	5	2	1	2
15	2020-05-24 17:01:15.606632	7	2	1	2
16	2020-05-24 17:01:19.608311	5	2	1	2
17	2020-05-24 17:01:20.60874	5	2	1	2
18	2020-05-24 17:01:21.609103	5	2	1	2
19	2020-05-24 17:01:22.609351	5	2	1	2
20	2020-05-24 17:01:23.61008	5	2	1	2
21	2020-05-24 17:01:24.610268	7	2	1	2
22	2020-05-24 17:01:26.611049	5	2	1	2
23	2020-05-24 17:01:27.611381	5	2	1	2
24	2020-05-24 17:01:28.611727	5	2	1	2
25	2020-05-24 17:01:29.611885	5	2	1	2
26	2020-05-24 17:01:30.612497	5	2	1	2
27	2020-05-24 17:04:48.639357	5	2	1	1
28	2020-05-24 17:05:06.743392	5	2	1	1
29	2020-05-24 17:05:07.744009	5	2	1	1
30	2020-05-24 17:05:08.744449	5	2	1	1
31	2020-05-24 17:05:09.744782	5	2	1	1
32	2020-05-24 17:05:09.75854	8	2	1	1
33	2020-05-24 17:05:10.745501	5	2	1	1
34	2020-05-24 17:05:10.770588	8	2	1	1
35	2020-05-24 17:05:11.746024	7	2	1	1
36	2020-05-24 17:05:11.765896	9	2	1	1
37	2020-05-24 17:28:03.748366	5	2	1	1
38	2020-05-24 17:28:21.840465	5	2	1	1
39	2020-05-24 17:28:22.840724	5	2	1	1
40	2020-05-24 17:28:23.84119	5	2	1	1
41	2020-05-24 17:28:24.84138	5	2	1	1
42	2020-05-24 17:28:24.860083	8	2	1	1
43	2020-05-24 17:28:25.841772	5	2	1	1
44	2020-05-24 17:28:25.859143	8	2	1	1
45	2020-05-24 17:28:26.841982	7	2	1	1
46	2020-05-24 17:28:26.860062	9	2	1	1
47	2020-05-24 18:55:29.276802	5	2	1	2
48	2020-05-24 18:55:30.397772	8	2	1	2
49	2020-05-24 18:55:31.376293	5	2	1	2
50	2020-05-24 18:55:31.39823	8	2	1	2
51	2020-05-24 23:02:40.255057	5	2	1	1
52	2020-05-24 23:02:58.351232	5	2	1	1
53	2020-05-24 23:02:59.351692	5	2	1	1
54	2020-05-24 23:03:00.352426	5	2	1	1
55	2020-05-24 23:03:01.352746	5	2	1	1
56	2020-05-24 23:03:01.372672	8	2	1	1
57	2020-05-24 23:03:02.353042	5	2	1	1
58	2020-05-24 23:03:02.374032	8	2	1	1
59	2020-05-24 23:03:03.353325	7	2	1	1
60	2020-05-24 23:03:03.375405	9	2	1	1
61	2020-05-24 23:03:44.617224	5	2	1	2
62	2020-05-24 23:03:46.694715	5	2	1	2
63	2020-05-24 23:03:47.695072	5	2	1	2
64	2020-05-24 23:03:48.695498	5	2	1	2
65	2020-05-24 23:03:49.696137	5	2	1	2
66	2020-05-24 23:03:50.696267	7	2	1	2
67	2020-05-24 23:04:02.05816	5	2	3	2
68	2020-05-24 23:04:04.139527	5	2	3	2
69	2020-05-24 23:04:05.1398	5	2	3	2
70	2020-05-24 23:04:06.140192	5	2	3	2
71	2020-05-24 23:04:07.140385	5	2	3	2
72	2020-05-24 23:04:08.140664	5	2	3	2
73	2020-05-24 23:04:09.140907	5	2	3	2
74	2020-05-24 23:04:10.141308	5	2	3	2
75	2020-05-24 23:04:11.141691	7	2	3	2
76	2020-05-24 23:04:14.142874	5	2	3	2
77	2020-05-24 23:04:14.165733	8	2	3	2
78	2020-05-24 23:04:15.143624	5	2	3	2
79	2020-05-24 23:04:15.161495	9	2	3	2
80	2020-05-24 23:04:16.143914	5	2	3	2
81	2020-05-24 23:04:17.144221	7	2	3	2
82	2020-05-24 23:04:18.144843	5	2	3	2
83	2020-05-24 23:04:19.145087	5	2	3	2
84	2020-05-24 23:04:20.145495	5	2	3	2
85	2020-05-24 23:04:21.145776	5	2	3	2
86	2020-05-24 23:04:22.145992	5	2	3	2
87	2020-05-24 23:04:23.146398	5	2	3	2
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
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.event (eventid, description) FROM stdin;
1	patient added
2	patient removed
3	monitor added
4	monitor removed
5	alarm set on
6	alarm cancelled by user
7	alarm set off
8	critical alarm set on
9	critical alarm set off
100	staff began shift
101	staff left shift
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
1	Alice
2	Bob
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

COPY public.staffevent (staffeventid, eventtime, eventtype, staffid) FROM stdin;
1	2020-05-25 11:28:00	1	1
2	2020-05-25 11:31:00	100	3
\.


--
-- Name: bed_bedid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bed_bedid_seq', 1, false);


--
-- Name: bedevent_bedeventid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bedevent_bedeventid_seq', 87, true);


--
-- Name: bedmodule_bedmoduleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bedmodule_bedmoduleid_seq', 1, false);


--
-- Name: module_moduleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.module_moduleid_seq', 1, false);


--
-- Name: modulemonitor_modulemonitorid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.modulemonitor_modulemonitorid_seq', 1, false);


--
-- Name: monitortype_monitortypeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.monitortype_monitortypeid_seq', 1, false);


--
-- Name: patient_patientid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.patient_patientid_seq', 1, false);


--
-- Name: shift_shiftid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shift_shiftid_seq', 1, false);


--
-- Name: staff_staffid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.staff_staffid_seq', 1, false);


--
-- Name: staffevent_staffeventid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.staffevent_staffeventid_seq', 2, true);


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
-- Name: event description_uq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT description_uq UNIQUE (description);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (eventid);


--
-- Name: bedevent eventtype_ck; Type: CHECK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE public.bedevent
    ADD CONSTRAINT eventtype_ck CHECK (((eventtype >= 1) AND (eventtype <= 9))) NOT VALID;


--
-- Name: CONSTRAINT eventtype_ck ON bedevent; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON CONSTRAINT eventtype_ck ON public.bedevent IS 'ensure eventtype has a valid value';


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

